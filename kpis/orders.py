from supabase import Client
import json

def count_total_orders(supabase: Client, organization_id: int = -1):
    try:
        if organization_id == -1:
            response = supabase.table('orders').select('*', count='exact').execute()
        else:
            response = supabase.table('orders').select('*', count='exact').eq('organization_id', organization_id).execute()
        return int(response.count)
    except:
        return Exception('Error while counting total orders')

def count_fringuant_orders(supabase: Client, organization_id: int = -1):
    try:
        if organization_id == -1:
            response = supabase.table('orders').select('data').execute()
        else:
            response = supabase.table('orders').select('data').eq('organization_id', organization_id).execute()

        count = 0
        for row in response.data:
            count += 1
            # if '_added_via_fringuant' in row:
            #     count += 1
        
        return count
    except Exception as e:
        return f"Error while counting total orders: {str(e)}"
