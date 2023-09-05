import string
import random
from hashlib import sha256
from re import search

def generer_mot_de_passe(longueur, inclure_chiffres, inclure_symboles):

    if longueur <= 0:
        raise ValueError("La taille du mot de passe doit être supérieur à 0")

    # Base du mot de passe : lettres majuscules et minuscules
    password = string.ascii_letters
    
    # Ajout des chiffres et des symboles si demandé
    if inclure_chiffres:
        password += string.digits

    # Ajout des symboles si demandé
    if inclure_symboles:
        password += string.punctuation

    password = ''.join(random.choice(password) for _ in range(int(longueur)))

    # Vérification que le mot de passe est sécurisé
    if not any(c.isupper() for c in password):
        raise ValueError("Le mot de passe doit contenir au moins une lettre majuscule")
    if not any(c.islower() for c in password):
        raise ValueError("Le mot de passe doit contenir au moins une lettre minuscule")
    

    if inclure_chiffres and not any(c.isdigit() for c in password):
        raise ValueError("Le mot de passe doit contenir au moins un chiffre")
    if inclure_symboles and not any(c in string.punctuation for c in password):
        raise ValueError("Le mot de passe doit contenir au moins un symbole")

    return password

    # Génération du mot de passe à partir de la base de caractères

def hash_password(pwd):
    return sha256(pwd.encode('utf-8')).hexdigest()

def demande_input(prompt):
    res = input(prompt).lower()

    if search(r'\d', res):
        raise ValueError("La réponse ne doit pas être un nombre")

    return res