from unittest import TestCase
from src.application import Application
from src.utilitaire import contains_digits, contains_symboles

class TestTkinter(TestCase):

    def tearDown(self) -> None:
        """
        Détruit l'application tkinter après chaque test.
        """
        self.tk.app.destroy()

    def setUp(self):
        """
        Initialise l'application pour les tests.
        """
        self.tk = Application()

    def test_slider(self):
        """
        Vérifie le fonctionnement du slider pour la longueur du mot de passe.
        """
        # Vérifie que la longueur par défaut du mot de passe est de 14 caractères
        self.assertEqual(self.tk.slider_longueur.get(), 14, f"La taille par défaut est de 14, non {self.tk.slider_longueur.get()}")

        # Déplace le slider pour changer la longueur du mot de passe
        self.tk.slider_longueur.set(20)

        # Vérifie que la longueur affichée est mise à jour en conséquence
        self.assertEqual(self.tk.slider_longueur.get(), 20, f"La taille du slider n'a pas été mise à jour, obtenu {self.tk.slider_longueur.get()}")

    def test_slider_label(self):
        """
        Vérifie le fonctionnement du slider pour la longueur du mot de passe.
        """
        # Déplace le slider pour changer la longueur du mot de passe
        self.tk.slider_longueur.set(21)

        self.assertEqual(self.tk.lbl_slider_value.cget("text"), "21", f"La taille du mot de passe a été définie à 21, obtenu : {self.tk.lbl_slider_value.cget('text')}")

    def test_default_password(self):
        """
        Vérifie la génération du mot de passe par défaut.
        """
        pwd = self.tk.lbl_resultat.cget("text")

        self.assertIsNotNone(pwd)
        self.assertGreaterEqual(len(pwd), 14, f"La taille par défaut du mot de passe est de 14 : {pwd}, taille : {len(pwd)}")

    def test_instanciate_element(self):
        """
        Vérifie si les éléments de l'interface sont instanciés correctement.
        """
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

    def test_checkboxes_default_values(self):
        """
        Vérifie que les cases à cocher "Inclure des chiffres" et "Inclure des symboles" ne sont pas cochées par défaut.
        """
        self.assertFalse(self.tk.chk_chiffres_var.get(), "Par défaut, les cases à cocher ne sont pas cochées")
        self.assertFalse(self.tk.chk_symboles_var.get(), "Par défaut, les cases à cocher ne sont pas cochées")

    def test_checkboxes_only_letter(self):
        """
        Vérifie que le mot de passe généré ne contient que des lettres lorsque les cases à cocher "Inclure des chiffres" et "Inclure des symboles" ne sont pas cochées.
        """
        self.tk.chk_chiffres_var.set(False)
        self.tk.chk_symboles_var.set(False)
        self.assertTrue(self.tk.lbl_resultat.cget("text").isalpha(), f"Le mot de passe ne contient pas seulement des lettres {self.tk.lbl_resultat.cget('text')}")

    def test_checkboxes_with_symboles(self):
        """
        Vérifie que le mot de passe généré contient au moins un caractère spécial lorsque la case à cocher "Inclure des symboles" est cochée.
        """
        self.tk.chk_symboles_var.set(True)
        self.assertTrue(contains_symboles(self.tk.lbl_resultat.cget("text")), f"Aucun caractère spécial n'a été trouvé dans {self.tk.lbl_resultat.cget('text')}")

    def test_checkboxes_with_digits(self):
        """
        Vérifie que le mot de passe généré contient au moins un chiffre lorsque la case à cocher "Inclure des chiffres" est cochée.
        """
        self.tk.chk_chiffres_var.set(True)
        self.assertTrue(contains_digits(self.tk.lbl_resultat.cget("text")), f"Aucun nombre n'a été trouvé dans {self.tk.lbl_resultat.cget('text')}")

    def test_checkboxes_with_digits_and_symboles(self):
        """
        Vérifie que le mot de passe généré contient au moins un chiffre et un caractère spécial lorsque les deux cases à cocher sont cochées.
        """

        for _ in range(155):
            self.tk.chk_chiffres_var.set(True)
            self.tk.chk_symboles_var.set(True)

            self.assertTrue(contains_symboles(self.tk.lbl_resultat.cget("text")), f"Aucun caractère spécial n'a été trouvé dans {self.tk.lbl_resultat.cget('text')}")
            self.assertTrue(contains_digits(self.tk.lbl_resultat.cget("text")), f"Aucun nombre n'a été trouvé dans {self.tk.lbl_resultat.cget('text')}")

            self.tk.chk_chiffres_var.set(False)
            self.tk.chk_symboles_var.set(False)

    def test_copy_button(self):
        """
        Vérifie que le bouton "Copier" copie le mot de passe généré dans le presse-papiers.
        """
        self.assertEqual(self.tk.app.clipboard_get(), self.tk.lbl_resultat.cget("text"), f"La copie de {self.tk.lbl_resultat.cget('text')} dans le presse-papier n'a pas fonctionné.")

    def test_refresh_hash(self):
        """
        Vérifie le changement de hachage et s'assure que le texte est différent.
        """
        pwd_hash_sha256 = self.tk.lbl_resultat_hash.cget("text")

        self.tk.combo_hashage.set("md5")

        self.tk.combo_hashage.event_generate("<<ComboboxSelected>>")

        self.assertNotEqual(pwd_hash_sha256, self.tk.lbl_resultat_hash.cget("text"), f"Les hachages doivent être différents, hachage 1 : {pwd_hash_sha256} hachage 2 : {self.tk.lbl_resultat_hash.cget('text')}")

    def test_title(self):
        """
        Vérifie le titre de l'application.
        """
        expected = "Générateur de mot de passe"
        self.assertEqual(self.tk.app.winfo_toplevel().title(), expected, f"Le titre de l'application doit être : {expected}")
