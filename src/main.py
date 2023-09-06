import tkinter as tk
from tkinter import ttk
from .utils import generer_mot_de_passe, hash_password

def mise_a_jour_mot_de_passe(*args):
    """
    Met à jour le mot de passe généré et son hachage, puis copie le mot de passe dans le presse-papier.
    """
    try:        
        # Récupérer les valeurs des widgets
        longueur = slider_longueur.get()
        inclure_chiffres = chk_chiffres_var.get()
        inclure_symboles = chk_symboles_var.get()
        # Générer le mot de passe
        mot_de_passe = generer_mot_de_passe(longueur, inclure_chiffres, inclure_symboles)
        # Afficher le mot de passe généré
        lbl_resultat.config(text=mot_de_passe)

        # Hachage du mot de passe
        methode_hashage = combo_hashage.get()

        if not methode_hashage:
            combo_hashage.set("sha256")
            methode_hashage = "sha256"
        
        lbl_resultat_hash.config(text=hash_password(mot_de_passe, methode_hashage))
        copier_presse_papier()
    except:
        pass


def refresh_hash(*args):
    """
    Rafraîchit le hachage du mot de passe affiché en fonction de la méthode de hachage sélectionnée.
    """
    methode_hashage = combo_hashage.get()
    if methode_hashage:
        # Mettre à jour l'affichage du hachage
        lbl_resultat_hash.config(text=hash_password(lbl_resultat.cget("text"), methode_hashage))
        

def update_slider_label(val):
    """
    Met à jour l'étiquette du curseur et déclenche la mise à jour du mot de passe en cas de changement de valeur.
    
    :param val: Nouvelle valeur du curseur.
    """
    if int(float(val)) == int(float(lbl_slider_value.cget("text"))):
        return
       
    #try:
        # Jouer un son si la valeur du curseur est 21 (Easter egg)
    #    if int(float(val)) == 21:
    #        Thread(target=playsound, args=("song/lit.mp3",), daemon=True).start()
    #except:
    #    print("No sound to play")

    # Mettre à jour l'étiquette du curseur
    lbl_slider_value.config(text=str(int(float(val))))

    # Mettre à jour le mot de passe en fonction de la nouvelle valeur du curseur
    mise_a_jour_mot_de_passe()

def copier_presse_papier():
    """
    Copie le mot de passe généré dans le presse-papier de l'application.
    """
    mot_de_passe = lbl_resultat.cget("text")

    # Effacer le presse-papier et y ajouter le mot de passe généré
    app.clipboard_clear()
    app.clipboard_append(mot_de_passe)

app = tk.Tk()
app.title("Générateur de mot de passe")

# Fixer la taille de la fenêtre
app.geometry("400x300")
app.configure(bg='#FCFCFD')
app.resizable(False, True)

# Configuration du style avec un autowrap, un fond blanc et une police Arial
style = ttk.Style()
style.theme_use("default")
style.configure("TFrame", background="#FCFCFD")
style.configure("TLabel", background="#FCFCFD", foreground="#1D1D1F", font=("Arial", 12), wraplength=300)
style.configure("TCheckbutton", background="#FCFCFD", foreground="#1D1D1F", font=("Arial", 12))
style.configure("TButton", font=("Arial", 12, "bold"))
style.configure("TScale", background="#ECECEF", troughcolor="#D9D9DA", sliderlength=20)

# Création du frame principal
frame = ttk.Frame(app, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Label pour afficher la longueur du mot de passe
lbl_longueur = ttk.Label(frame, text="Longueur du mot de passe ")
lbl_longueur.grid(column=0, row=0, sticky=tk.W, pady=5)

# Label pour afficher la valeur du slider
lbl_slider_value = ttk.Label(frame, text="14")
lbl_slider_value.grid(column=2, row=0, pady=5)

# Slider pour choisir la longueur du mot de passe
slider_longueur = ttk.Scale(frame, from_=12, to_=30, orient=tk.HORIZONTAL, command=update_slider_label)
slider_longueur.set(14)
slider_longueur.grid(column=1, row=0, sticky=(tk.W, tk.E), pady=5)

# Checkbox pour inclures ou non les chiffres
chk_chiffres_var = tk.BooleanVar()
chk_chiffres_var.trace_add("write", mise_a_jour_mot_de_passe)
chk_chiffres = ttk.Checkbutton(frame, text="Inclure des chiffres", variable=chk_chiffres_var)
chk_chiffres.grid(column=0, row=1, sticky=tk.W, pady=5)

# Checkbox pour inclures ou non les symboles
chk_symboles_var = tk.BooleanVar()
chk_symboles_var.trace_add("write", mise_a_jour_mot_de_passe)
chk_symboles = ttk.Checkbutton(frame, text="Inclure des symboles", variable=chk_symboles_var)
chk_symboles.grid(column=1, row=1, sticky=tk.W, pady=5)

# Sélecteur de méthode de hachage
lbl_hashage = ttk.Label(frame, text="Méthode de hachage :")
lbl_hashage.grid(column=0, row=2, sticky=tk.W, pady=5)
combo_hashage = ttk.Combobox(frame, values=["md5", "sha1", "sha224", "sha256", "sha384", "sha512", "blake2b", "blake2s", "sha3_224", "sha3_256", "sha3_384", "sha3_512", "shake_128", "shake_256"], state="readonly")
combo_hashage.grid(column=1, row=2, sticky=(tk.W, tk.E), pady=5)
combo_hashage.bind("<<ComboboxSelected>>", refresh_hash)

# Label pour afficher le mot de passe généré
lbl_resultat = ttk.Label(frame, text="", font=("Arial", 14, "bold"))
lbl_resultat.grid(column=0, row=3, columnspan=2, pady=5)

# Label pour afficher le hash du mot de passe généré
lbl_resultat_hash = ttk.Label(frame, text="", font=("Arial", 14, "italic"))
lbl_resultat_hash.grid(column=0, row=5, columnspan=3, pady=5)

# Bouton pour copier le mot de passe dans le presse-papier
btn_copier = ttk.Button(frame, text="Copier", command=copier_presse_papier)
btn_copier.grid(column=0, row=6, pady=5, columnspan=3)

# Générer un premier mot de passe au lancement de l'application
mise_a_jour_mot_de_passe()

# Lancer la boucle principale de l'application
app.mainloop()