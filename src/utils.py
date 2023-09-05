import string
import random
from hashlib import sha256

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