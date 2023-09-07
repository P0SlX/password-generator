import string
import random
import hashlib
from re import search

def generer_mot_de_passe(longueur, inclure_chiffres, inclure_symboles):
    """
    Génère un mot de passe aléatoire en utilisant les options spécifiées.
    
    :param longueur: Longueur du mot de passe à générer.
    :param inclure_chiffres: Indique si le mot de passe doit inclure des chiffres (True/False).
    :param inclure_symboles: Indique si le mot de passe doit inclure des symboles (True/False).
    :return: Le mot de passe généré.
    :raises ValueError: Si la longueur spécifiée est inférieure ou égale à 0.
    """
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


def hash_password(pwd, hash_method='sha256'):
    """
    Hashe le mot de passe fourni en utilisant l'algorithme de hachage spécifié.
    
    :param pwd: Mot de passe à hasher.
    :param hash_method: Algorithme de hachage à utiliser (par défaut: 'sha256').
    :return: Le hachage en format hexadécimal du mot de passe.
    """
    hasher = hashlib.new(hash_method)
    hasher.update(pwd.encode('utf-8'))
    return hasher.hexdigest()

def demande_input(prompt):
    """
    Demande à l'utilisateur une entrée en minuscules et vérifie si elle contient des nombres.
    
    :param prompt: Le message à afficher pour demander l'entrée.
    :return: L'entrée de l'utilisateur en minuscules, si elle ne contient pas de nombres.
    :raises ValueError: Si l'entrée de l'utilisateur contient des nombres.
    """
    res = input(prompt).lower()

    if search(r'\d', res):
        raise ValueError("La réponse ne doit pas être un nombre")

    return res

def contains_symboles(pwd):
    return any(c in "!@#$%^&*()_+-=[]{};:,.<>/?\\" for c in pwd)

def contains_digits(pwd):
    return any(c.isdigit() for c in pwd)

def notation_password(pwd):
    if len(pwd) <= 8:
        return "#FA5339"

    if contains_symboles() and contains_digits():
        return "#4DFA46"
    
    return "#C74B1C"