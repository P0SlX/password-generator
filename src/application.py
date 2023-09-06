import sys

sys.path.append(".")

import tkinter as tk
from tkinter import ttk
from src.utilitaire import generer_mot_de_passe, hash_password

class Application():

    app = None
    frame = None

    lbl_slider_value = None
    slider = None
    
    chk_chiffres = None
    chk_chiffres_var = None

    chk_symboles = None
    chk_symboles_var = None

    lbl_resultat = None

    combo_hashage = None
    lbl_hashage = None

    lbl_resultat_hash = None

    def __init__(self) -> None:
        self.app = tk.Tk()

        self.__load_parameters()
        self.__load_style()
        self.__load_frame()
        self.__load_labels()
        self.__load_slider()
        self.__load_checkbox()
        self.__load_select_hash()
        self.__load_button()

        # Générer un premier mot de passe au lancement de l'application
        self.__mise_a_jour_mot_de_passe()

    def __load_parameters(self):
        self.app.title("Générateur de mot de passe")

        # Fixer la taille de la fenêtre
        self.app.geometry("400x300")
        self.app.configure(bg='#FCFCFD')
        self.app.resizable(False, True)

    # Configuration du style avec un autowrap, un fond blanc et une police Arial
    def __load_style(self):
        style = ttk.Style()
        style.theme_use("default")
        style.configure("TFrame", background="#FCFCFD")
        style.configure("TLabel", background="#FCFCFD", foreground="#1D1D1F", font=("Arial", 12), wraplength=300)
        style.configure("TCheckbutton", background="#FCFCFD", foreground="#1D1D1F", font=("Arial", 12))
        style.configure("TButton", font=("Arial", 12, "bold"))
        style.configure("TScale", background="#ECECEF", troughcolor="#D9D9DA", sliderlength=20)

    def __load_frame(self):
        # Création du frame principal
        self.frame = ttk.Frame(self.app, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    def __load_labels(self):
        # Label pour afficher la longueur du mot de passe
        lbl_longueur = ttk.Label(self.frame, text="Longueur du mot de passe ")
        lbl_longueur.grid(column=0, row=0, sticky=tk.W, pady=5)

        # Label pour afficher la valeur du slider
        self.lbl_slider_value = ttk.Label(self.frame, text="14")
        self.lbl_slider_value.grid(column=2, row=0, pady=5)

        # Label pour afficher le mot de passe généré
        self.lbl_resultat = ttk.Label(self.frame, text="", font=("Arial", 14, "bold"))
        self.lbl_resultat.grid(column=0, row=3, columnspan=2, pady=5)

        # Label pour afficher le hash du mot de passe généré
        self.lbl_resultat_hash = ttk.Label(self.frame, text="", font=("Arial", 14, "italic"))
        self.lbl_resultat_hash.grid(column=0, row=5, columnspan=3, pady=5)

    def __load_slider(self):
        # Slider pour choisir la longueur du mot de passe
        self.slider_longueur = ttk.Scale(self.frame, from_=12, to_=30, orient=tk.HORIZONTAL, command=self.__update_slider_label)
        self.slider_longueur.set(14)
        self.slider_longueur.grid(column=1, row=0, sticky=(tk.W, tk.E), pady=5)

    def __load_checkbox(self):
        # Checkbox pour inclures ou non les chiffres
        self.chk_chiffres_var = tk.BooleanVar()
        self.chk_chiffres_var.trace_add("write", self.__mise_a_jour_mot_de_passe)
        self.chk_chiffres = ttk.Checkbutton(self.frame, text="Inclure des chiffres", variable=self.chk_chiffres_var)
        self.chk_chiffres.grid(column=0, row=1, sticky=tk.W, pady=5)

        # Checkbox pour inclures ou non les symboles
        self.chk_symboles_var = tk.BooleanVar()
        self.chk_symboles_var.trace_add("write", self.__mise_a_jour_mot_de_passe)
        self.chk_symboles = ttk.Checkbutton(self.frame, text="Inclure des symboles", variable=self.chk_symboles_var)
        self.chk_symboles.grid(column=1, row=1, sticky=tk.W, pady=5)

    def __load_select_hash(self):
        # Sélecteur de méthode de hachage
        self.lbl_hashage = ttk.Label(self.frame, text="Méthode de hachage :")
        self.lbl_hashage.grid(column=0, row=2, sticky=tk.W, pady=5)
        
        self.combo_hashage = ttk.Combobox(self.frame, values=["md5", "sha1", "sha224", "sha256", "sha384", "sha512", "blake2b", "blake2s", "sha3_224", "sha3_256", "sha3_384", "sha3_512", "shake_128", "shake_256"], state="readonly")
        self.combo_hashage.grid(column=1, row=2, sticky=(tk.W, tk.E), pady=5)
        self.combo_hashage.bind("<<ComboboxSelected>>", self.__refresh_hash)


    def __load_button(self):
        # Bouton pour copier le mot de passe dans le presse-papier
        btn_copier = ttk.Button(self.frame, text="Copier", command=self.__copier_presse_papier)
        btn_copier.grid(column=0, row=6, pady=5, columnspan=3)


    def __mise_a_jour_mot_de_passe(self,*args):
        """
        Met à jour le mot de passe généré et son hachage, puis copie le mot de passe dans le presse-papier.
        """
        try:        
            # Récupérer les valeurs des widgets
            longueur = self.slider_longueur.get()
            inclure_chiffres = self.chk_chiffres_var.get()
            inclure_symboles = self.chk_symboles_var.get()
            # Générer le mot de passe
            mot_de_passe = generer_mot_de_passe(longueur, inclure_chiffres, inclure_symboles)
            # Afficher le mot de passe généré
            self.lbl_resultat.config(text=mot_de_passe)

            # Hachage du mot de passe
            methode_hashage = self.combo_hashage.get()

            if not methode_hashage:
                self.combo_hashage.set("sha256")
                methode_hashage = "sha256"
            
            self.lbl_resultat_hash.config(text=hash_password(mot_de_passe, methode_hashage))
            self.__copier_presse_papier()
        except:
            pass

    def __update_slider_label(self,val):
        """
        Met à jour l'étiquette du curseur et déclenche la mise à jour du mot de passe en cas de changement de valeur.
        
        :param val: Nouvelle valeur du curseur.
        """
        if int(float(val)) == int(float(self.lbl_slider_value.cget("text"))):
            return

        # Mettre à jour l'étiquette du curseur
        self.lbl_slider_value.config(text=str(int(float(val))))

        # Mettre à jour le mot de passe en fonction de la nouvelle valeur du curseur
        self.__mise_a_jour_mot_de_passe()

    def __refresh_hash(self,*args):
        """
        Rafraîchit le hachage du mot de passe affiché en fonction de la méthode de hachage sélectionnée.
        """
        methode_hashage = self.combo_hashage.get()
        if methode_hashage:
            # Mettre à jour l'affichage du hachage
            self.lbl_resultat_hash.config(text=hash_password(self.lbl_resultat.cget("text"), methode_hashage))

    def __copier_presse_papier(self):
        """
        Copie le mot de passe généré dans le presse-papier de l'application.
        """
        mot_de_passe = self.lbl_resultat.cget("text")

        # Effacer le presse-papier et y ajouter le mot de passe généré
        self.app.clipboard_clear()
        self.app.clipboard_append(mot_de_passe)

    # Lancer la boucle principale de l'application
    def run(self) -> None:
        self.app.mainloop()