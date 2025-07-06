# PFE_AVM_2023 : Site Web de Vente de Carburants et Lubrifiants Aviation & Marine

## 🎯 Description du Projet
Ce projet est une application web dynamique développée dans le cadre de mon **Mémoire de Licence en Ingénierie des Systèmes d'Information et des Logiciels** à l'Université des Sciences et de la Technologie Houari Boumediene (USTHB). Il s'agit d'un site de vente en ligne des produits carburants et lubrifiants destinés aux secteurs de l'aviation et de la marine, conçu pour l'organisme **NAFTAL Branche Carburants**.

Le travail a été réalisé il y a environ 3 ans (soutenance le 05/06/2023).

## 💻 Technologies Utilisées
Ce projet a été développé en utilisant les technologies suivantes :
* **Python**
* **Django** (framework web)
* **HTML, CSS, JavaScript** (pour le frontend)
* **MySQL** (base de données relationnelle)

## 📁 Structure du Répertoire
Voici un aperçu de la structure principale du code :

PFE_AVM_2023-main/
├── src/                       # Répertoire principal du code source Django
│   ├── Produit/               # Application Django pour la gestion des produits
│   ├── User_Aviation/         # Application Django pour les utilisateurs aviation/marine
│   ├── admin_app/             # Application Django pour l'interface d'administration
│   └── manage.py              # Utilitaire de ligne de commande Django
├── env_pfeavm/                # Environnement virtuel Python (ignoré par Git)
├── .gitignore                 # Fichiers et dossiers à ignorer par Git
├── README.md                  # Ce fichier
└── requirements.txt           # Dépendances Python du projet


\## 🛠️ Guide d'Installation et d'Exécution (pour information)

\*Note : Ces étapes décrivent comment le projet était mis en place et exécuté au moment de sa conception.\*



1\.  \*\*Cloner le dépôt :\*\*

&nbsp;   ```bash

&nbsp;   git clone \[https://github.com/votre\_nom\_utilisateur/PFE\_AVM\_2023.git](https://github.com/votre\_nom\_utilisateur/PFE\_AVM\_2023.git)

&nbsp;   ```

2\.  \*\*Accéder au répertoire du projet :\*\*

&nbsp;   ```bash

&nbsp;   cd PFE\_AVM\_2023

&nbsp;   ```

3\.  \*\*Créer et activer un environnement virtuel :\*\*

&nbsp;   ```bash

&nbsp;   python -m venv env\_pfeavm

&nbsp;   # Pour Windows :

&nbsp;   .\\env\_pfeavm\\Scripts\\activate

&nbsp;   # Pour Linux/macOS :

&nbsp;   source env\_pfeavm/bin/activate

&nbsp;   ```

4\.  \*\*Installer les dépendances :\*\*

&nbsp;   ```bash

&nbsp;   pip install -r requirements.txt

&nbsp;   ```

5\.  \*\*Appliquer les migrations de la base de données :\*\*

&nbsp;   ```bash

&nbsp;   python src/manage.py migrate

&nbsp;   ```

6\.  \*\*Démarrer le serveur de développement :\*\*

&nbsp;   ```bash

&nbsp;   python src/manage.py runserver

&nbsp;   ```

&nbsp;   L'application serait alors accessible via votre navigateur à `http://127.0.0.1:8000/`.



\## 🤝 Auteurs

\* \*\*DIGUER Nedjemddine\*\*

\* \*\*LAIB Ayoub\*\*



\## 🙏 Remerciements

Nous tenons à exprimer notre sincère gratitude à notre promoteur, Monsieur BRADAIE Mustapha, pour son précieux encadrement et son soutien tout au long de la réalisation de ce Projet de Fin d'Études.

