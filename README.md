# Setup du projet

## Cloner le dépôt

Clonez le dépôt avec la commande suivante :

```sh
git clone git@github.com:PierreLouisLetoquart/KPIs.git
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

## Fonctions proposées

Le folder `interfaces` est en cours de developpement. Les fonctions proposées ne sont pas tester et pas forcemment fonctionnelles!

### utils/supabaseClient

| Fonction | Inputs | Outputs | Description |
| --- | --- | --- | --- |
| `create_supabase_client` | None | Client | Crée un client supabase pour communiquer avec la bdd grace aux variables d'environnement |

### utils/supabaseDataloader

| Fonction | Inputs | Outputs | Description |
| --- | --- | --- | --- |
| `fetch_logs` | supabase (Client), organization (str) | pd.DataFrame | Récupère tous les logs de Supabase pour une organisation spécifique. |
| `fetch_orders` | supabase (Client), organization_id (int) | pd.DataFrame | Récupère toutes les commandes de Supabase pour une organisation spécifique. |
| `store_data_to_csv` | data (pd.DataFrame), file_path (str) | None | Stocke le dataframe d'entrée sous forme de fichier CSV au chemin de fichier spécifié. |

### utils/kpis

| Fonction                      | Inputs            | Outputs                                | Description                                                                                                |
| -----------------------------|------------------|----------------------------------------| -----------------------------------------------------------------------------------------------------------|
| `count_total_records`           | filename (str)    | int                                    | Compte le nombre total d'enregistrements dans le fichier spécifié.                                         |
| `count_records_by_type`         | filename (str)    | dict                                   | Retourne un dictionnaire avec le nombre d'enregistrements par type d'action du fichier csv spécifié.      |
| `count_records_by_organization` | filename (str)    | dict                                   | Compte le nombre d'enregistrements pour chaque organisation dans un fichier CSV.                           |
| `count_records_by_date`         | filename (str)    | dict                                   | Compte le nombre d'enregistrements pour chaque date dans un fichier CSV.                                   |
| `count_distinct_types`          | filename (str)    | set                                    | Compte les types distincts dans un fichier CSV et les renvoie sous forme de set.                            |
