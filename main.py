import setup
from utils.supabaseClient import create_supabase_client
from utils.supabaseDataloader import fetch_logs, fetch_orders, store_data_to_csv

supabase_client = create_supabase_client()

logs_df = fetch_logs(supabase_client, organization="cotele")
orders_df = fetch_orders(supabase_client, organization_id=10)

store_data_to_csv(logs_df, "./extract_KPIs/tests/logs.csv")
store_data_to_csv(orders_df, "./extract_KPIs/tests/orders.csv")