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
    return ''.join(random.choice(caracteres) for _ in range(longueur))

def hash_password(pwd):
    return sha256(pwd.encode('utf-8')).hexdigest()

def main():
    # Longueur du mot de passe
    longueur = int(input("Entrez la longueur souhaitée pour le mot de passe : "))
    
    # Inclure les chiffres dans le mot de passe final ?
    inclure_chiffres = input("Voulez-vous inclure des chiffres ? (O/n) ").lower() == "o"
    
    # Inclure les symboles dans le mot de passe final ?
    inclure_symboles = input("Voulez-vous inclure des symboles ? (O/n) ").lower() == "o"
    
    # Mot de passe généré
    mot_de_passe = generer_mot_de_passe(longueur, inclure_chiffres, inclure_symboles)
    
    print(f"Mot de passe généré : {mot_de_passe}")

if __name__ == "__main__":
    main()
