import setup
from utils.supabaseDataloader import fetch_orders, store_data_to_csv
from utils.supabaseClient import create_supabase_client

# Point d'entrée du programme
if __name__ == "__main__":
    logs = fetch_orders(create_supabase_client(), 10)
    store_data_to_csv(logs, "data/logs2.csv")
