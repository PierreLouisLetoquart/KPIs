# Exctraction de KPIs

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

Le folder `interfaces` est en cours de developpement. Les fonctions proposées ne sont pas fonctionnelles!

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

### kpis/basics

| Fonction | Inputs | Outputs | Description |
| --- | --- | --- | --- |
| `count_button_display` | supabase: Client, organization: str='all' | int | Compte le nombre total de fois où le bouton a été affiché. 20% est retiré du fait du bot Google, etc... |
| `count_button_clicked` | supabase: Client, organization: str='all' | int | Compte le nombre total de fois où le bouton a été cliqué. |
| `count_user_scan` | supabase: Client, organization: str='all' | int | Compte le nombre total de fois où l'utilisateur s'est scanné. |

### kpis/orders

| Fonction | Inputs | Outputs | Description |
| --- | --- | --- | --- |
| `count_total_orders` | filename: str | int | Compte le nombre total de commandes dans un fichier CSV. Renvoie 0 si le fichier n'est pas trouvé. |
| `count_fringuant_orders` | filename: str | int | Compte le nombre de commandes effectuées grâce à Fringuant dans un fichier CSV. Renvoie 0 si le fichier n'est pas trouvé. |
