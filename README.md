# Python Functions Fringuant

## Setup du projet

1. Clonez le dépôt avec la commande suivante :

```sh
git clone git@github.com:PierreLouisLetoquart/KPIs.git
```

2. Créez un environnement virtuel

```sh
python3 -m venv env
```

3. Activez l'environnement virtuel

```sh
source env/bin/activate # Unix based systems
env\Scripts\activate.bat # Windows
```

4. Installez les dépendances

```sh
pip install -r requirements.txt
```

5. Configurez les variables d'env

```sh
mv .env.example .env
```

*Une fois la commande précédente executée, allez compléter les variables dans `./.env`*

## Fonctions proposées

### utils/supabase

Ces fonctions permettent de prendre les données de Supabase et de les télécharger en local.

| Fonction | Inputs | Outputs | Description |
| --- | --- | --- | --- |
| `create_supabase_client` | None | Client | Crée un client supabase pour communiquer avec la bdd grace aux variables d'environnement |
| `fetch_logs` | supabase (Client), organization (str) | pd.DataFrame | Récupère tous les logs de Supabase pour une organisation spécifique. |
| `fetch_orders` | supabase (Client), organization_id (int) | pd.DataFrame | Récupère toutes les commandes de Supabase pour une organisation spécifique. |
| `store_data_to_csv` | data (pd.DataFrame), file_path (str) | None | Stocke le dataframe d'entrée sous forme de fichier CSV au chemin de fichier spécifié. |

### utils/data_filters

Ces fonctions sont utiles pour prétraiter les *logs* et *orders* avant de les sauveguarder dans supabase.

| Fonction        | Inputs                           | Outputs                             | Description                                                                      |
| ---             | ---                              | ---                                 | ---                                                                              |
| `filter_order`    | input: json                      | json                                | Filtre et renvoie un objet JSON contenant uniquement les informations pertinentes d'une commande. |
| `filter_logs`     | input: json                      | json                                | Filtre et renvoie un objet JSON contenant uniquement les informations pertinentes d'un journal d'activité (log). |
| `load_json_file`  | filename: str                    | dict                                | Charge le contenu d'un fichier JSON dans un dictionnaire Python.                   |
| `save_json_file`  | json_data: dict, filename: str   | None                                | Enregistre un dictionnaire Python dans un fichier JSON avec un nom de fichier spécifié. |

### utils/period_filters

Ces fonctions permettent de filtrer et retourner uniquement le dataset sur la periode qui nous interesse.

**Warning**, la fonction `filter_csv_with_period` est un peu du bricolage.

**TODO**: réorganiser le code pour que load_csv soit a la bonne place et revoir les valeurs de retour + date format.

| Fonction | Inputs | Outputs | Description |
| --- | --- | --- | --- |
| `load_csv` | `filename: str` | `List[List[str]]` | Charge des données à partir d'un fichier CSV et renvoie une liste de listes.|
| `check_csv_has_created_at_column` | `input_data: List[List[str]]` | `bool` | Vérifie si une liste de listes contenant des données d'un fichier CSV a une colonne 'created_at'. |
| `get_period_filter` | `period_type: str` | `Tuple[datetime, datetime]` | Retourne un tuple d'objets datetime de début et de fin en fonction du type de période donné. |
| `filter_csv_with_period` | `input_data: List[List[str]], date_range: Tuple[datetime, datetime]` | `List[List[str]]` | Filtre les données d'un fichier CSV en fonction de la plage de dates spécifiée. |

### kpis/basics

**Warning**, Utilise l'API supabase, n'utilise pas l'extract local en csv. (À update)

**WIP**, ces fonctions sont en cours de dev, pas de temporalitée ni de filtrage avancé!

| Fonction | Inputs | Outputs | Description |
| --- | --- | --- | --- |
| `count_button_display` | supabase: Client, organization: str='all' | int | Compte le nombre total de fois où le bouton a été affiché. 20% est retiré du fait du bot Google, etc... |
| `count_button_clicked` | supabase: Client, organization: str='all' | int | Compte le nombre total de fois où le bouton a été cliqué. |
| `count_user_scan` | supabase: Client, organization: str='all' | int | Compte le nombre total de fois où l'utilisateur s'est scanné. |

### kpis/orders

**WIP**, ces fonctions sont en cours de dev, pas de temporalitée ni de filtrage avancé!

| Fonction | Inputs | Outputs | Description |
| --- | --- | --- | --- |
| `count_total_orders` | filename: str | int | Compte le nombre total de commandes dans un fichier CSV. Renvoie 0 si le fichier n'est pas trouvé. |
| `count_fringuant_orders` | filename: str | int | Compte le nombre de commandes effectuées grâce à Fringuant dans un fichier CSV. Renvoie 0 si le fichier n'est pas trouvé. |
