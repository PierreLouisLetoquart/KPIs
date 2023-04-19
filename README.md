# Exctraction de KPIs

## Setup du projet

Clonez le dépôt avec la commande suivante :

```sh
git clone git@github.com:PierreLouisLetoquart/KPIs.git
```

Créez un environnement virtuel

```sh
python3 -m venv env
```

Activez l'environnement virtuel

```sh
source env/bin/activate # Unix based systems
env\Scripts\activate.bat # Windows
```

Installez les dépendances

```sh
pip install -r requirements.txt
```

Configurez les variables d'env

```sh
mv .env.example .env
```

Une fois la commande précédente executée, allez compléter les variables dans `./.env`

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
