from utils.supabaseClient import create_supabase_client
from kpis.orders import count_orders, count_total_orders__
from utils.supabaseDataloader import fetch_orders, store_data_to_csv

# Point d'entrée du programme
if __name__ == "__main__":
    file = 'data/orders2.csv'
    supabase_client = create_supabase_client()
    df = fetch_orders(supabase_client, 14)
    store_data_to_csv(df, file)
    print(count_total_orders__(file))