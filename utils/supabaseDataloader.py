import os
import pandas as pd
from supabase import Client

def fetch_logs(supabase: Client, organization: str) -> pd.DataFrame:
    """
    Fetches all logs from Supabase for a specific organization.

    Parameters:
        supabase (Client): The Supabase client instance.
        organization (str): The name of the organization.

    Returns:
        pd.DataFrame: A Pandas DataFrame containing the logs data.
    """
    print(f"Fetching logs for organization: {organization}")
    logs = []
    logs_response = supabase.table("logs").select("*").eq("organization", organization).execute()
    logs.extend(logs_response.data)
    
    df_logs = pd.DataFrame(logs)

    # correct typo
    df_logs.loc[df_logs.type == 'FINGUANT_BUTTON_CLICKED', 'type'] = 'FRINGUANT_BUTTON_CLICKED'
    df_logs.loc[df_logs.type == 'FINGUANT_BUTTON_DISPLAYED', 'type'] = 'FRINGUANT_BUTTON_DISPLAYED'

    return df_logs

def fetch_orders(supabase: Client, organization_id: int) -> pd.DataFrame:
    """
    Fetches all orders from Supabase for a specific organization.

    Parameters:
        supabase (Client): The Supabase client instance.
        organization_id (int): The ID of the organization to fetch orders for.

    Returns:
        pd.DataFrame: A Pandas DataFrame containing the orders data.
    """
    print(f"Fetching orders for organization ID: {organization_id}")
    orders = []
    orders_response = supabase.table("orders").select("*").eq("organization_id", organization_id).execute()
    orders.extend(orders_response.data)
    
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
