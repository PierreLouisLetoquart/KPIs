# Setup du projet

## Cloner le dépôt

Clonez le dépôt avec la commande suivante :

```sh
git clone https://github.com/username/projet.git
```

## Créer un environnement virtuel

Il est recommandé de créer un environnement virtuel pour isoler les dépendances du projet. Pour créer un environnement virtuel, utilisez la commande suivante :

```sh
python3 -m venv env
```

Cette commande va créer un dossier `env` dans votre répertoire actuel.

### Activer l'environnement virtuel

Activez l'environnement virtuel en utilisant la commande suivante :

```sh
source env/bin/activate # Unix based systems
env\Scripts\activate.bat # Windows
```

Vous verrez que le nom de votre environnement virtuel s'affichera dans votre invite de commande.

## Installer les dépendances

Une fois l'environnement virtuel activé, vous pouvez installer les dépendances du projet en utilisant la commande suivante :

```sh
pip install -r requirements.txt
```

Assurez-vous que vous vous trouvez dans le répertoire du projet pour exécuter cette commande.

## Configuration

Avant de lancer le projet, vous devez configurer les variables d'environnement dans un fichier .env. Copiez le fichier .env.example et renommez-le en .env, puis modifiez les variables selon vos besoins.

```sh
mv .env.example .env
```

## Lancer le projet

Vous pouvez lancer le projet en exécutant la commande suivante :

```sh
python main.py
```

Assurez-vous que vous vous trouvez dans le répertoire du projet pour exécuter cette commande.

## Désactiver l'environnement virtuel

Lorsque vous avez fini de travailler sur le projet, vous pouvez désactiver l'environnement virtuel en utilisant la commande suivante :

```sh
deactivate
```
