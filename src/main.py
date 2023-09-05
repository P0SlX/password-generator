import string
import random
from hashlib import sha256
import tkinter as tk
from tkinter import ttk

def generer_mot_de_passe(longueur, inclure_chiffres, inclure_symboles):
    # Base du mot de passe : lettres majuscules et minuscules
    caracteres = string.ascii_letters
    
    # Ajout des chiffres et des symboles si demandé
    if inclure_chiffres:
        caracteres += string.digits

    # Ajout des symboles si demandé
    if inclure_symboles:
        caracteres += string.punctuation

    # Génération du mot de passe à partir de la base de caractères
    return ''.join(random.choice(caracteres) for _ in range(int(longueur)))

def hash_password(pwd):
    return sha256(pwd.encode('utf-8')).hexdigest()

def mise_a_jour_mot_de_passe():
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