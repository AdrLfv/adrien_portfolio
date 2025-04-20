# Guide de déploiement sur Hostinger

Ce document explique comment déployer ce portfolio Flask sur Hostinger.

## Étape 1: Générer les fichiers statiques

Exécutez le script de génération de site statique :

```bash
python generate_static_site.py
```

Ce script va créer un dossier `static_html` contenant votre site converti en HTML statique.

## Étape 2: Télécharger les fichiers sur Hostinger

1. Connectez-vous à votre compte Hostinger et accédez au gestionnaire de fichiers
2. Uploadez les fichiers suivants à la racine de votre hébergement:
   - Le fichier `index.php` (qui va rediriger les requêtes)
   - Le dossier `static_html` (contenant votre site statique)

## Étape 3: Configuration des URLs

Si vous avez besoin d'utiliser un domaine personnalisé:

1. Dans le panneau de contrôle Hostinger, allez dans "Domaines" 
2. Configurez votre nom de domaine pour qu'il pointe vers votre hébergement

## Structure des fichiers

Votre hébergement Hostinger devrait maintenant avoir cette structure:

```
public_html/
├── index.php                 # Script PHP qui gère les routes
└── static_html/              # Votre site converti en HTML statique
    ├── index.html            # Page d'accueil
    ├── about.html            # Page À propos
    ├── cv.html               # Page CV
    ├── contact.html          # Page Contact
    ├── project_1.html        # Page du projet 1
    ├── project_2.html        # Page du projet 2
    ├── ...
    ├── 404.html              # Page d'erreur 404
    └── static/               # Ressources statiques (CSS, JS, images)
        ├── css/
        ├── js/
        └── images/
```

## Notes importantes

- Si vous modifiez votre site Flask, vous devrez regénérer les fichiers statiques et les télécharger à nouveau.
- Cette solution ne gère pas les fonctionnalités dynamiques côté serveur comme les formulaires de contact.
- Pour les formulaires, envisagez d'utiliser un service externe comme Formspree ou d'ajouter un script PHP pour gérer l'envoi d'emails.
