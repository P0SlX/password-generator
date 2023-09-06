from unittest import TestCase
from re import search
from src.utils import generer_mot_de_passe, hash_password
from hashlib import sha256

class TestGenererMotsDePasse(TestCase):

    def test_lettre(self):
        """
        Vérifie que le mot de passe généré ne contient que des lettres.
        """
        password = generer_mot_de_passe(5, False, False)

        # Vérifier que le mot de passe ne contient que des lettres
        match = search(r'\d', password)
        self.assertIsNone(match, "Le mot de passe ne doit contenir que des lettres: " + password)

    def test_caractere_speciaux(self):
        """
        Vérifie que le mot de passe généré contient au moins un caractère spécial.
        """
        password = generer_mot_de_passe(10, False, True)

        # Vérifier que le mot de passe contient au moins un caractère spécial
        match = search(r'[^\w\s]', password)
        self.assertIsNotNone(match, "Le mot de passe doit contenir au moins un caractère spécial: " + password)

    def test_taille(self):
        """
        Vérifie que le mot de passe généré a la longueur correcte.
        """
        password = generer_mot_de_passe(15, False, False)

        # Vérifier que le mot de passe a la longueur correcte
        self.assertEqual(len(password), 15, "Le mot de passe doit avoir une longueur de 15 caractères: " + password)

    def test_hash(self):
        """
        Vérifie que le mot de passe généré est correctement haché en utilisant SHA256.
        """
        password = generer_mot_de_passe(8, False, True)

        # Hacher le mot de passe en utilisant SHA256
        hashed_password = sha256(password.encode()).hexdigest()

        pwd = hash_password(password)

        # Vérifier que le mot de passe est un hachage SHA256
        self.assertEqual(hashed_password, pwd, "Le mot de passe doit être un hash SHA256: " + password)

    def test_type(self):
        """
        Vérifie que le mot de passe généré est de type chaîne de caractères.
        """
        password = generer_mot_de_passe(8, False, True)

        self.assertIsInstance(password, str, "Le mot de passe doit être une chaîne de caractères")

    def test_taille_negative(self):
        """
        Vérifie que la génération avec une taille négative lève une exception ValueError.
        """
        self.assertRaises(ValueError, generer_mot_de_passe, -5, False, True)

    def test_taille_large(self):
        """
        Vérifie si une grande taille est prise en charge par Python.
        """
        password = generer_mot_de_passe(3_000_000, False, True)
        self.assertEqual(len(password), 3_000_000)
