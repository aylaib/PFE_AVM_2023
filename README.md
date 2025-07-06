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



=======
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
├── docs/                      # Contient le rapport final du PFE
│   └── Memoire_046.pdf
├── src/                       # Répertoire principal du code source Django
│   ├── admin_app/             # Application pour l'interface d'administration
│   ├── media/                 # Fichiers médias (images, etc.) téléchargés
│   ├── Produit/               # Application gérant les produits
│   ├── project/               # Configuration principale du projet Django
│   │   ├── settings.py        # Fichier de configuration
│   │   └── urls.py            # Routes URL principales
│   ├── user_app/              # Application pour l'interface utilisateur
│   ├── User_Aviation/         # Application spécifique à la gestion des utilisateurs/aviation
│   └── manage.py              # Utilitaire d'administration Django
├── requirements.txt           # Liste des dépendances Python du projet
└── .gitignore                 # Fichiers et dossiers à ignorer par Git
└── README.md                  # Ce fichier


## 🛠️ Guide d'Installation et d'Exécution (pour information)
*Note : Ces étapes décrivent comment le projet était mis en place et exécuté au moment de sa conception.*

1.  **Cloner le dépôt :**
    ```bash
    git clone [https://github.com/votre_nom_utilisateur/PFE_AVM_2023.git](https://github.com/votre_nom_utilisateur/PFE_AVM_2023.git)
    ```
2.  **Accéder au répertoire du projet :**
    ```bash
    cd PFE_AVM_2023
    ```
3.  **Créer et activer un environnement virtuel :**
    ```bash
    python -m venv env_pfeavm
    # Pour Windows :
    .\env_pfeavm\Scripts\activate
    # Pour Linux/macOS :
    source env_pfeavm/bin/activate
    ```
4.  **Installer les dépendances :**
    ```bash
    pip install -r requirements.txt
    ```
5.  **Appliquer les migrations de la base de données :**
    ```bash
    python src/manage.py migrate
    ```
6.  **Démarrer le serveur de développement :**
    ```bash
    python src/manage.py runserver
    ```
    L'application serait alors accessible via votre navigateur à `http://127.0.0.1:8000/`.

## 🤝 Auteurs
* **DIGUER Nedjemddine**
* **LAIB Ayoub**

## 🙏 Remerciements
Nous tenons à exprimer notre sincère gratitude à notre promoteur, Monsieur BRADAIE Mustapha, pour son précieux encadrement et son soutien tout au long de la réalisation de ce Projet de Fin d'Études.
>>>>>>> f2f2148ca4842fddcbc625ce0f3cc163bc0cff9b
