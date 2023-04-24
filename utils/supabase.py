import os
import pandas as pd
from supabase import create_client, Client
from dotenv import load_dotenv

def create_supabase_client() -> Client:
    """
    Crée un client Supabase à partir des variables d'environnement SUPABASE_URL et SUPABASE_KEY.

    Returns:
    -------
    Client :
        Un client Supabase
    """
    try:
        load_dotenv()
        supabase_url = os.environ.get("SUPABASE_URL")
        supabase_key = os.environ.get("SUPABASE_ANON_KEY")
        return create_client(supabase_url, supabase_key)
    except Exception as e:
        print(f"Erreur lors de la création du client Supabase : {str(e)}")
        return None

def fetch_logs(supabase: Client, organization: str = "all") -> pd.DataFrame:
    """
    Fetches all logs from Supabase for a specific organization. If no organization is specified, all logs are fetched.

    Parameters:
        supabase (Client): The Supabase client instance.
        organization (str): The name of the organization. Defaults to "all".

    Returns:
        pd.DataFrame: A Pandas DataFrame containing the logs data.
    """
    print(f"Fetching logs: ", end="", flush=True)
    logs = []
    start_index = 0
    while True:
        if(organization == "all"):
            logs_response = supabase.table("logs").select("*").range(start_index, start_index + 1000).execute()
        else:
            logs_response = supabase.table("logs").select("*").range(start_index, start_index + 1000).eq("organization", organization).execute()
        new_logs = logs_response.data
        logs.extend(new_logs)
        if len(new_logs) == 0:
            break
        start_index += 1000
        print("=", end="", flush=True)
    print("")

    df_logs = pd.DataFrame(logs)

    # correct typo
    df_logs.loc[df_logs.type == 'FINGUANT_BUTTON_CLICKED', 'type'] = 'FRINGUANT_BUTTON_CLICKED'
    df_logs.loc[df_logs.type == 'FINGUANT_BUTTON_DISPLAYED', 'type'] = 'FRINGUANT_BUTTON_DISPLAYED'

    return df_logs

def fetch_orders(supabase: Client, organization_id: int = -1) -> pd.DataFrame:
    """
    Fetches all orders from Supabase for a specific organization. If no organization is specified, all orders are fetched.

    Parameters:
        supabase (Client): The Supabase client instance.
        organization_id (int): The ID of the organization to fetch orders for. Defaults to -1.

    Returns:
        pd.DataFrame: A Pandas DataFrame containing the orders data.
    """
    print(f"Fetching orders: ", end="", flush=True)
    orders = []
    start_index = 0
    while True:
        if(organization_id == -1):
            orders_response = supabase.table("orders").select("*").range(start_index, start_index + 1000).execute()
        else:
            orders_response = supabase.table("orders").select("*").range(start_index, start_index + 1000).eq("organization_id", organization_id).execute()
        new_orders = orders_response.data
        orders.extend(new_orders)
        if len(new_orders) == 0:
            break
        start_index += 1000
        print("=", end="", flush=True)
    print("")
    
    df_orders = pd.DataFrame(orders)

    return df_orders

def store_data_to_csv(data: pd.DataFrame, file_path: str):
    """
    Stores the input dataframe as a CSV file at the specified file path.

    Args:
        data (pandas.DataFrame): The input dataframe to store as a CSV file.
        file_path (str): The file path to save the CSV file to.
    """
    try:
        # Extract the directory from the file path
        directory = os.path.dirname(file_path)

        # Create the directory if it doesn't exist
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Created directory: {directory}")

        # Save the data to the CSV file
        data.to_csv(file_path, index=False)
        print(f"Data saved successfully to {file_path}")

    except Exception as e:
        print(f"Error while saving data to {file_path}: {e}")
