from utils.supabaseClient import create_supabase_client
from kpis.orders import count_total_orders
from utils.supabaseDataloader import fetch_logs, store_data_to_csv

# Point d'entrée du programme
if __name__ == "__main__":
    file = 'data/logs.csv'
    supabase_client = create_supabase_client()
    df = fetch_logs(supabase_client)
    store_data_to_csv(df, file)
    print(count_total_orders(file))