from unittest import TestCase
from re import search
from ..src.main import generer_mot_de_passe

class TestGenererMotsDePasse(TestCase):

    def test_lettre(self):
        password = generer_mot_de_passe(5, False, False)

        # Check that the password only contains letters
        match = search(r'[^a-zA-Z]', password)
        self.assertIsNone(match, "Le mot de passe ne doit contenir que des lettres: " + password)

    def test_caractere_speciaux(self):
        password = generer_mot_de_passe(10, True, False)

        # Check that the password contains at least one special character
        match = search(r'[^\w\s]', password)
        self.assertIsNotNone(match, "Le mot de passe doit contenir au moins un caractère spécial: " + password)

    def test_taille(self):
        password = generer_mot_de_passe(15, False, False)

        # Check that the password has the correct length
        self.assertEqual(len(password), 15, "Le mot de passe doit avoir une longueur de 15 caractères: " + password)

    def test_hash(self):
        password = generer_mot_de_passe(8, False, True)

        # Check that the password is hashed
        self.assertTrue(password.startswith("$2"), "Le mot de passe doit être hashé: " + password)