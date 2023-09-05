import string
import random
from hashlib import sha256
from re import search

def generer_mot_de_passe(longueur, inclure_chiffres, inclure_symboles):

    if longueur <= 0:
        raise ValueError("La taille du mot de passe doit être supérieur à 0")

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

def demande_input(prompt):
    res = input(prompt).lower()

    if search(r'\d', res):
        raise ValueError("La réponse ne doit pas être un nombre")

    return res