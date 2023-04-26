import pandas as pd

def count_button_displayed(dataset: pd.DataFrame, organization: str = "all") -> int:
    try:
        count = 0
        for row in dataset:
            if(row['organization'] == organization):
                if row['type'] == 'FRINGUANT_BUTTON_DISPLAYED':
                    count += 1
        return count
    except FileNotFoundError:
        raise Exception(f"An error occured while opening the file {dataset}")

def count_button_clicked():
    return 0

def count_user_scan():
    return 0

from supabase import Client
from typing import Optional

def fetch_supabase_logs(supabase: Client, organization: Optional[str] = None, start_date: Optional[str] = None, end_date: Optional[str] = None) -> pd.DataFrame:
    logs = []
    start_index = 0

    # Basic querry to fetch all logs
    query = supabase.table("logs").select("*").range(start_index, start_index + 1000)

    # Add optional filters to the querry
    if organization is not None:
        query = query.eq("organization", organization)
    if start_date is not None:
        query = query.gte("created_at", start_date)
    if end_date is not None:
        query = query.lte("created_at", end_date)

    while True:
        # Execute the querry
        response = query.execute()
        new_logs = response.data
        logs.extend(new_logs)

        if len(new_logs) == 0:
            break

        start_index += 1000
        print(f"Fetching logs from index {start_index}")

    # Convert the response to a pandas dataframe
    df_logs = pd.DataFrame(logs)

    # correct typo
    df_logs.loc[df_logs.type == 'FINGUANT_BUTTON_CLICKED', 'type'] = 'FRINGUANT_BUTTON_CLICKED'
    df_logs.loc[df_logs.type == 'FINGUANT_BUTTON_DISPLAYED', 'type'] = 'FRINGUANT_BUTTON_DISPLAYED'

    return df_logs
