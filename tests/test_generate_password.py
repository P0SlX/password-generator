from unittest import TestCase
from re import search
from src.utils import generer_mot_de_passe, hash_password
from hashlib import sha256

class TestGenererMotsDePasse(TestCase):

    def test_lettre(self):
        password = generer_mot_de_passe(5, False, False)

        # Check that the password only contains letters
        match = search(r'\d', password)
        self.assertIsNone(match, "Le mot de passe ne doit contenir que des lettres: " + password)

    def test_caractere_speciaux(self):
        password = generer_mot_de_passe(10, False, True)

        # Check that the password contains at least one special character
        match = search(r'[^\w\s]', password)
        self.assertIsNotNone(match, "Le mot de passe doit contenir au moins un caractère spécial: " + password)

    def test_taille(self):
        password = generer_mot_de_passe(15, False, False)

        # Check that the password has the correct length
        self.assertEqual(len(password), 15, "Le mot de passe doit avoir une longueur de 15 caractères: " + password)

    def test_hash(self):
        password = generer_mot_de_passe(8, False, True)

        # Hash the password using SHA256
        hashed_password = sha256(password.encode()).hexdigest()

        pwd = hash_password(password)

        # Check that the password is a SHA256 hash
        self.assertEqual(hashed_password, pwd, "Le mot de passe doit être un hash SHA256: " + password)

    # Check if generate password is string
    def test_type(self):
        password = generer_mot_de_passe(8, False, True)

        self.assertIsInstance(password, str, "Le mot de passe doit être une chaîne de caractères")