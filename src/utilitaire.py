import string
import random
import hashlib
from re import search

def generer_mot_de_passe(longueur: int, inclure_chiffres, inclure_symboles):
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

    # Shuffle de la base de caractères et on trim la longueur
    longueur = int(longueur)
    caracteres = ''.join(random.sample(string.ascii_letters*(max(longueur, len(string.ascii_letters))), longueur))
    position_deja_modifiee = []
    
    # Ajout des chiffres et des symboles si demandé
    if inclure_chiffres:
        # On ajoute des chiffres à des positions aléatoires et on mémorise les positions déjà modifiées
        for _ in range(random.randint(1, longueur // 4)):
            position = random.randint(0, len(caracteres) - 1)
            while position in position_deja_modifiee:
                position = random.randint(0, len(caracteres) - 1)
            caracteres = caracteres[:position] + random.choice("0123456789") + caracteres[position + 1:]
            position_deja_modifiee.append(position)
            

    # Ajout des symboles si demandé
    if inclure_symboles:
        # On ajoute des symboles à des positions aléatoires et on mémorise les positions déjà modifiées
        for _ in range(random.randint(1, longueur // 4)):
            position = random.randint(0, len(caracteres) - 1)
            while position in position_deja_modifiee:
                position = random.randint(0, len(caracteres) - 1)
            caracteres = caracteres[:position] + random.choice("!@#$%^&*()_+-=[]{};:,.<>/?\\") + caracteres[position + 1:]
    

    # Génération du mot de passe à partir de la base de caractères
    return caracteres

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
    """
    Vérifie si une chaîne de caractères contient au moins un caractère spécial.

    :param pwd: La chaîne de caractères à vérifier.
    :type pwd: str

    :return: True si la chaîne contient au moins un caractère spécial, False sinon.
    :rtype: bool
    """
    return any(c in "!@#$%^&*()_+-=[]{};:,.<>/?\\" for c in pwd)

def contains_digits(pwd):
    """
    Vérifie si une chaîne de caractères contient au moins un chiffre.

    :param pwd: La chaîne de caractères à vérifier.
    :type pwd: str

    :return: True si la chaîne contient au moins un chiffre, False sinon.
    :rtype: bool
    """
    return any(c.isdigit() for c in pwd)

def notation_password(pwd):
    """
    Détermine la couleur de notation pour un mot de passe en fonction de sa longueur et de son contenu.

    :param pwd: Le mot de passe à noter.
    :type pwd: str

    :return: La couleur de notation au format hexadécimal.
    :rtype: str
    """
    if len(pwd) >= 12 or (len(pwd) > 8 and (contains_symboles(pwd) or contains_digits(pwd))):
        return "#3bc736"  # Vert
    
    if len(pwd) > 8:
        return "#C74B1C"  # Orange
    
    return "#FF0000"  # Rouge
