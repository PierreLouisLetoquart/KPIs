from utils.supabaseDataloader import fetch_logs, store_data_to_csv
from utils.supabaseClient import create_supabase_client
from utils.logKpis import count_records_by_type

def example():
    filename = "data/logs.csv"
    client = create_supabase_client()

    dataframe = fetch_logs(client, 'cotele')
    store_data_to_csv(dataframe, filename)

    output = count_records_by_type(filename)
    print(output)

# Point d'entrée du programme
if __name__ == "__main__":
    example()