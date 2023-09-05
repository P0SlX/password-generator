from unittest import TestCase
from src.utils import demande_input
from unittest.mock import patch

class TestInput(TestCase):
    
    @patch('builtins.input', side_effect=["3"])
    def test_nombre(self, mock_input):
        self.assertRaises(ValueError, demande_input, "Voulez vous ajouter des caractères spéciaux ?")

    @patch('builtins.input', side_effect=["o"])
    def test_lettre(self, mock_input):
        res = demande_input("Voulez vous ajouter des caractères spéciaux ?")

        self.assertEqual(res, "o")

    @patch('builtins.input', side_effect=["O"])
    def test_lower(self, mock_input):
        res = demande_input("Voulez vous ajouter des caractères spéciaux ?")

        self.assertEqual(res, "o")