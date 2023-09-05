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
