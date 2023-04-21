from utils.supabaseClient import create_supabase_client
from kpis.orders import count_fringuant_orders

# Point d'entrée du programme
if __name__ == "__main__":
    supabase_client = create_supabase_client()
    print(count_fringuant_orders(supabase_client, -1))