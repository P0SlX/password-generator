import tkinter as tk
from tkinter import ttk
from utils import generer_mot_de_passe, hash_password

def mise_a_jour_mot_de_passe(*args):
    try:        
        # Récupérer les valeurs des widgets
        longueur = slider_longueur.get()
        inclure_chiffres = chk_chiffres_var.get()
        inclure_symboles = chk_symboles_var.get()
        # Générer le mot de passe
        mot_de_passe = generer_mot_de_passe(longueur, inclure_chiffres, inclure_symboles)
        # Afficher le mot de passe généré
        lbl_resultat.config(text=mot_de_passe)
        lbl_resultat_hash.config(text=hash_password(mot_de_passe))
    except:
        pass

def update_slider_label(val):
    lbl_slider_value.config(text=str(int(float(val))))
    mise_a_jour_mot_de_passe()

app = tk.Tk()
app.title("Générateur de mot de passe")

# Configuration du style
style = ttk.Style()
style.configure("TFrame", background="#FCFCFD")
style.configure("TLabel", background="#FCFCFD", foreground="#1D1D1F", font=("Arial", 12))
style.configure("TCheckbutton", background="#FCFCFD", foreground="#1D1D1F", font=("Arial", 12))
style.configure("TButton", font=("Arial", 12, "bold"))
style.configure("TScale", background="#ECECEF", troughcolor="#D9D9DA", sliderlength=20)


frame = ttk.Frame(app, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

lbl_longueur = ttk.Label(frame, text="Longueur du mot de passe :")
lbl_longueur.grid(column=0, row=0, sticky=tk.W, pady=5)

# Label pour afficher la valeur du slider
lbl_slider_value = ttk.Label(frame, text="14")
lbl_slider_value.grid(column=2, row=0, pady=5)

# Slider pour choisir la longueur du mot de passe
slider_longueur = ttk.Scale(frame, from_=12, to_=128, orient=tk.HORIZONTAL, command=update_slider_label)
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

# Label pour afficher le mot de passe généré
lbl_resultat = ttk.Label(frame, text="", font=("Arial", 14, "bold"))
lbl_resultat.grid(column=0, row=3, columnspan=3, pady=5)

lbl_resultat_hash = ttk.Label(frame, text="", font=("Arial", 14, "bold"))
lbl_resultat_hash.grid(column=0, row=4, columnspan=3, pady=5)

# Générer un premier mot de passe au lancement de l'application
mise_a_jour_mot_de_passe()
# Lancer la boucle principale de l'application
app.mainloop()