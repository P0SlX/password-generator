# Générateur de Mots de Passe Sécurisés en Python

## Description

Ce projet est un générateur de mots de passe sécurisés avec une interface utilisateur conviviale. L'utilisateur peut spécifier la longueur du mot de passe et choisir d'inclure des chiffres et/ou des symboles.

## Fonctionnalités

- **Interface Utilisateur** : Une interface graphique simple et intuitive permettant à l'utilisateur de définir la longueur du mot de passe et de choisir l'inclusion de chiffres et/ou de symboles.
  
- **Génération du Mot de Passe** : Le programme génère aléatoirement un mot de passe en fonction des paramètres spécifiés par l'utilisateur. Le mot de passe généré est conçu pour être fort et sécurisé.

- **Hashage (en option)** : L'utilisateur obtient le hash en SHA-256 en dessous de son mot de passe généré.

## Tests et Validation

Des tests approfondis ont été réalisés pour s'assurer que la génération de mots de passe fonctionne correctement. Les fonctionnalités liées aux chiffres et aux symboles ont également été testées.

## Utilisation

1. Lancez le programme.
2. Utilisez le slider pour définir la longueur souhaitée du mot de passe.
3. Sélectionnez si vous souhaitez inclure des chiffres et/ou des symboles.
4. Le mot de passe généré s'affichera automatiquement à chaque modification des paramètres.
5. Le mot de passe est **automatiquement** copié dans le presse-papier.
5. Si besoin, le bouton "Copier" permet de copier le mot de passe dans le presse-papier si celui-ci à été modifié.

## Documentation

Le code est documenté pour expliquer le fonctionnement de chaque fonction. Les dépendances nécessaires sont `tkinter` pour l'interface graphique et les modules `string` et `random` pour la génération du mot de passe.


## Tableau des tests unitaires

| Nom du cas du test | ID | Objectif | Préconditionnement | Action attendue du User | Action Système attendue | Données des tests | Critères de réussite | Status |
|--------------------|----|----------|--------------------|-------------------------|-------------------------|-------------------|----------------------|--------|
| Test Lettre | 1 | Vérifier que le mot de passe généré ne contient que des lettres | Aucun | Aucun | Générer un mot de passe | Longueur: 5, Chiffres: False, Symboles: False | Aucun chiffre dans le mot de passe | Réussi |
| Test Caractère Spéciaux | 2 | Vérifier que le mot de passe généré contient au moins un caractère spécial | Aucun | Aucun | Générer un mot de passe | Longueur: 10, Chiffres: False, Symboles: True | Au moins un caractère spécial dans le mot de passe | Réussi |
| Test Taille | 3 | Vérifier que le mot de passe généré a la longueur correcte | Aucun | Aucun | Générer un mot de passe | Longueur: 15, Chiffres: False, Symboles: False | Longueur du mot de passe = 15 | Réussi |
| Test Hash | 4 | Vérifier que le mot de passe généré est correctement haché en utilisant SHA256 | Aucun | Aucun | Générer et hacher un mot de passe | Longueur: 8, Chiffres: False, Symboles: True | Le hash du mot de passe correspond au hash SHA256 | Réussi |
| Test Type | 5 | Vérifier que le mot de passe généré est de type chaîne de caractères | Aucun | Aucun | Générer un mot de passe | Longueur: 8, Chiffres: False, Symboles: True | Le mot de passe est une chaîne de caractères | Réussi |
| Test Taille Négative | 6 | Vérifier que la génération avec une taille négative lève une exception ValueError | Aucun | Aucun | Lever une exception | Longueur: -5, Chiffres: False, Symboles: True | Une exception ValueError est levée | Réussi |
| Test Taille Large | 7 | Vérifier si une grande taille est prise en charge par Python | Aucun | Aucun | Générer un mot de passe | Longueur: 3_000_000, Chiffres: False, Symboles: True | Longueur du mot de passe = 3_000_000 | Réussi |
| Test Nombre | 8 | Vérifier que l'entrée non valide lève une exception ValueError | Aucun | Entrer "3" | Demander une entrée | "3" | Une exception ValueError est levée | Réussi |
| Test Lettre | 9 | Vérifier que l'entrée est correctement traitée | Aucun | Entrer "o" | Demander une entrée | "o" | L'entrée est "o" | Réussi |
| Test Lower | 10 | Vérifier que l'entrée est convertie en minuscule | Aucun | Entrer "O" | Demander une entrée | "O" | L'entrée est "o" | Réussi |
| Test Slider Default | 11 | Vérifier que la longueur par défaut du mot de passe est de 14 caractères | Aucun | Aucun | Vérifier la valeur du slider | Aucun | La valeur du slider est 14 | Réussi |
| Test Slider Update | 12 | Vérifier que le slider met à jour la longueur du mot de passe | Aucun | Déplacer le slider | Mettre à jour la valeur du slider | Nouvelle valeur: 20 | La valeur du slider est 20 | Réussi |
| Test Slider Label Update | 13 | Vérifier que le label du slider est mis à jour | Aucun | Déplacer le slider | Mettre à jour le label du slider | Nouvelle valeur: 21 | Le label affiche "21" | Réussi |
| Test Default Password | 14 | Vérifier que le mot de passe par défaut est généré | Aucun | Aucun | Afficher le mot de passe généré | Aucun | Le mot de passe est d'au moins 14 caractères | Réussi |
| Test Instanciate Element | 15 | Vérifier si les éléments sont instanciés | Aucun | Aucun | Instancier les éléments | Aucun | Tous les éléments sont instanciés | Réussi |
| Test Checkboxes Default | 16 | Vérifier que les checkboxes sont décochées par défaut | Aucun | Aucun | Vérifier l'état des checkboxes | Aucun | Les checkboxes sont décochées | Réussi |
| Test Checkboxes Letters Only | 17 | Vérifier que le mot de passe généré ne contient que des lettres si les checkboxes sont décochées | Aucun | Désactiver les checkboxes | Générer un mot de passe | Checkboxes: False | Le mot de passe ne contient que des lettres | Réussi |
| Test Checkboxes With Symbols | 18 | Vérifier que le mot de passe généré contient des symboles si la checkbox correspondante est cochée | Aucun | Activer la checkbox des symboles | Générer un mot de passe | Checkbox symboles: True | Le mot de passe contient au moins un symbole | Réussi |
| Test Checkboxes With Digits | 19 | Vérifier que le mot de passe généré contient des chiffres si la checkbox correspondante est cochée | Aucun | Activer la checkbox des chiffres | Générer un mot de passe | Checkbox chiffres: True | Le mot de passe contient au moins un chiffre | Réussi |
| Test Checkboxes Both | 20 | Vérifier que le mot de passe généré contient des chiffres et des symboles si les deux checkboxes sont cochées | Aucun | Activer les deux checkboxes | Générer un mot de passe | Checkboxes chiffres et symboles: True | Le mot de passe contient au moins un chiffre et un symbole | Réussi |
| Test Copy Button | 21 | Vérifier que le bouton "Copier" copie le mot de passe dans le presse-papier | Aucun | Cliquer sur le bouton "Copier" | Copier le mot de passe dans le presse-papier | Aucun | Le presse-papier contient le mot de passe généré | Réussi |
| Test Refresh Hash | 22 | Vérifier que le changement de hachage met à jour le texte du hash | Aucun | Changer le type de hachage | Mettre à jour le texte du hash | Nouveau hachage: md5 | Le texte du hash est différent de SHA256 | Réussi |
| Test Title | 23 | Vérifier que le titre de l'application est correct | Aucun | Aucun | Afficher le titre de l'application | Aucun | Le titre est "Générateur de mot de passe" | Réussi |
| Test Contains Digits | 24 | Vérifier si la fonction détecte des chiffres dans la chaîne | Aucun | Aucun | Exécuter la fonction `contains_digits` | "gfdhg12FDSGf" | La fonction retourne True | Réussi |
| Test Not Contains Digits | 25 | Vérifier si la fonction ne détecte pas de chiffres dans la chaîne | Aucun | Aucun | Exécuter la fonction `contains_digits` | "FFgfh$ùgfhfghkofh" | La fonction retourne False | Réussi |
| Test Contains Symboles | 26 | Vérifier si la fonction détecte des symboles dans la chaîne | Aucun | Aucun | Exécuter la fonction `contains_symboles` | "gfdg$$^gfdgd" | La fonction retourne True | Réussi |
| Test Not Contains Symboles | 27 | Vérifier si la fonction ne détecte pas de symboles dans la chaîne | Aucun | Aucun | Exécuter la fonction `contains_symboles` | "gfdgdfg1321" | La fonction retourne False | Réussi |
| Test Contains Symboles and Digits | 28 | Vérifier si la fonction détecte des chiffres et des symboles dans la chaîne | Aucun | Aucun | Exécuter les fonctions `contains_digits` et `contains_symboles` | "fdgfj1232FDGù^" | Les deux fonctions retournent True | Réussi |
| Test Notation Red | 29 | Vérifier si la notation du mot de passe est rouge | Aucun | Aucun | Exécuter la fonction `notation_password` | "1f$" | La fonction retourne "#FA5339" | Réussi |
| Test Notation Orange | 30 | Vérifier si la notation du mot de passe est orange | Aucun | Aucun | Exécuter la fonction `notation_password` | "gfgf12gmpolg" | La fonction retourne "#C74B1C" | Réussi |
| Test Notation Green | 31 | Vérifier si la notation du mot de passe est verte | Aucun | Aucun | Exécuter la fonction `notation_password` | "gr13GF^$5687lkj" | La fonction retourne "#4DFA46" | Réussi |