from unittest import TestCase
from src.application import Application
from pyvirtualdisplay import Display

class TestTkinter(TestCase):

    @classmethod
    def setUpClass(self):
        self.display = Display(visible=False, size=(1024, 768))
        self.display.start()
    
    @classmethod
    def tearDownClass(self):
        self.display.stop()

    def tearDown(self) -> None:
        self.tk.app.destroy()

    def setUp(self):
        self.tk = Application()

    def test_slider(self):
        # Check that the default password length is 14 characters
        self.assertEqual(self.tk.slider_longueur.get(), 14, f"La taille par défaut est de 14 non {self.tk.slider_longueur.get()}")

        # Move the slider to change the password length
        self.tk.slider_longueur.set(20)

        # Verify that the displayed length updates accordingly
        self.assertEqual(self.tk.slider_longueur.get(), 20, f"La taille du slider n'a pas été mise à jour obtenu {self.tk.slider_longueur.get()}")

    def test_slider_label(self):
        # Move the slider to change the password length
        self.tk.slider_longueur.set(21)

        self.assertEqual(self.tk.lbl_slider_value.cget("text"), "21", f"La taille du mot de passe a été set à 21 obtenu : {self.tk.lbl_slider_value.cget('text')}")

    def test_default_password(self):
        pwd = self.tk.lbl_resultat.cget("text")

        self.assertIsNotNone(pwd)
        self.assertGreaterEqual(len(pwd), 14, f"La taille par défaut du mot de passe est de 14 : {pwd}, taille : {len(pwd)}")
    
    # Check if element are instantiate
    def test_instanciate_element(self):
        self.assertIsNotNone(self.tk.app)
        self.assertIsNotNone(self.tk.lbl_slider_value)
        self.assertIsNotNone(self.tk.slider_longueur)
        self.assertIsNotNone(self.tk.chk_chiffres)
        self.assertIsNotNone(self.tk.chk_chiffres_var)
        self.assertIsNotNone(self.tk.chk_symboles)
        self.assertIsNotNone(self.tk.chk_symboles_var)
        self.assertIsNotNone(self.tk.lbl_resultat)
        self.assertIsNotNone(self.tk.combo_hashage)
        self.assertIsNotNone(self.tk.lbl_hashage)
        self.assertIsNotNone(self.tk.lbl_resultat_hash)

    # Check that the "Inclure des chiffres & Inclure des symboles" checkbox is unchecked by default
    def test_checkboxes_default_values(self):
        self.assertFalse(self.tk.chk_chiffres_var.get(), "Par défaut les checkbox ne sont pas cochées")
        self.assertFalse(self.tk.chk_symboles_var.get(), "Par défaut les checkbox ne sont pas cochées")

    # Check that the generated password only contains letters when the "Inclure des chiffres" and "Inclure des symboles" checkboxes are unchecked
    def test_checkboxes_only_letter(self):
        self.tk.chk_chiffres_var.set(False)
        self.tk.chk_symboles_var.set(False)
        self.assertTrue(self.tk.lbl_resultat.cget("text").isalpha(), f"Le mots de passe ne contient pas seulement des lettres {self.tk.lbl_resultat.cget('text')}")

    # Check that the generated password contains at least one special character when the "Inclure des symboles" checkbox is checked
    def test_checkboxes_with_symboles(self):
        self.tk.chk_symboles_var.set(True)
        self.assertTrue(any(c in "!@#$%^&*()_+-=[]{};:,.<>/?\\" for c in self.tk.lbl_resultat.cget("text")), f"Aucun caractère spécial n'a été trouvé dans {self.tk.lbl_resultat.cget('text')}")

    # Check that the generated password contains at least one digit when the "Inclure des chiffres" checkbox is checked
    def test_checkboxes_with_digits(self):
        self.tk.chk_chiffres_var.set(True)
        self.assertTrue(any(c.isdigit() for c in self.tk.lbl_resultat.cget("text")), f"Aucun nombre n'a été trouvé dans {self.tk.lbl_resultat.cget('text')}")

    # Check both cheboxes
    def test_checkboxes_with_digits_and_symboles(self):
        self.tk.chk_chiffres_var.set(True)
        self.tk.chk_symboles_var.set(True)

        self.assertTrue(any(c in "!@#$%^&*()_+-=[]{};:,.<>/?\\" for c in self.tk.lbl_resultat.cget("text")), f"Aucun caractère spécial n'a été trouvé dans {self.tk.lbl_resultat.cget('text')}")
        self.assertTrue(any(c.isdigit() for c in self.tk.lbl_resultat.cget("text")), f"Aucun nombre n'a été trouvé dans {self.tk.lbl_resultat.cget('text')}")

    # Click the "Copier" button and verify that the generated password is copied to the clipboard
    def test_copy_button(self):
        self.assertEqual(self.tk.app.clipboard_get(), self.tk.lbl_resultat.cget("text"), f"La copie de {self.tk.lbl_resultat.cget('text')} dans le presse papier n'a pas fonctionné.")

    # Change hash and check if text is different
    def test_refresh_hash(self):
        pwd_hash_sha256 = self.tk.lbl_resultat_hash.cget("text")

        self.tk.combo_hashage.set("md5")

        self.tk.combo_hashage.event_generate("<<ComboboxSelected>>")

        self.assertNotEqual(pwd_hash_sha256, self.tk.lbl_resultat_hash.cget("text"), f"Les hash doivent être différents hash 1: {pwd_hash_sha256} hash 2 :{self.tk.lbl_resultat_hash.cget('text')}")

    # Check the title 
    def test_title(self):
        expected = "Générateur de mot de passe"
        self.assertEqual(self.tk.app.winfo_toplevel().title(), expected, f"Le titire de l'application doit être : {expected}")
