from supabase import Client

def count_button_display(supabase: Client, organization: str = 'all') -> int:
    """
    Compte le nombre total de fois ou le bouton est apparu.
    20% est retiré du au bot google etc...

    Args:
        supabase (Client): client supabase pour effectuer les querry.
        organization (str, optional): L'organisation pour laquelle on veut compter les boutons display. Defaults to 'all'.

    Returns:
        int: le nombre de fois ou le bouton est apparu.

    """
    try:
        if organization == 'all':
            response = supabase.table('logs').select('*', count='exact').eq('type', 'FRINGUANT_BUTTON_DISPLAYED').execute()
        else:
            response = supabase.table('logs').select('*', count='exact').eq('type', 'FRINGUANT_BUTTON_DISPLAYED').eq('organization', organization).execute()
        return int(response.count * 0.8)
    except:
        return Exception('Error while counting button display')
    
def count_button_clicked(supabase: Client, organization: str = 'all') -> int:
    """
    Compte le nombre total de fois ou le bouton a été cliqué.

    Args:
        supabase (Client): client supabase pour effectuer les querry.
        organization (str, optional): L'organisation pour laquelle on veut compter les boutons clicked. Defaults to 'all'.

    Returns:
        int: le nombre de fois ou le bouton a été cliqué.

    """
    try:
        if organization == 'all':
            response = supabase.table('logs').select('*', count='exact').eq('type', 'FRINGUANT_BUTTON_CLICKED').execute()
        else:
            response = supabase.table('logs').select('*', count='exact').eq('type', 'FRINGUANT_BUTTON_CLICKED').eq('organization', organization).execute()
        return int(response.count)
    except:
        return Exception('Error while counting button clicked')
    
def count_user_scan(supabase: Client, organization: str = 'all') -> int:
    """
    Compte le nombre total de fois ou l'utilisateur s'est scanné'.

    Args:
        supabase (Client): client supabase pour effectuer les querry.
        organization (str, optional): L'organisation pour laquelle on veut compter le nbr de scans. Defaults to 'all'.

    Returns:
        int: le nombre de fois ou l'utilisateur s'est scanné.

    """
    try:
        if organization == 'all':
            response = supabase.table('logs').select('*', count='exact').eq('type', 'USER_HAS_MADE_A_SCAN').execute()
        else:
            response = supabase.table('logs').select('*', count='exact').eq('type', 'USER_HAS_MADE_A_SCAN').eq('organization', organization).execute()
        return int(response.count)
    except:
        return Exception('Error while counting user scan')
    
def get_basics_kpis(supabase: Client, organization: str = 'all') -> dict:
    """
    Retourne les kpis de base.

    Args:
        supabase (Client): client supabase pour effectuer les querry.
        organization (str, optional): L'organisation pour laquelle on veut compter le nbr de scans. Defaults to 'all'.

    Returns:
        dict: les kpis de base.

    """
    try:
        traffic = count_button_display(supabase, organization)
        conversion = count_button_clicked(supabase, organization) / traffic
        user_scan = count_user_scan(supabase, organization)
        return {
            'traffic': traffic,
            'conversion': conversion,
            'user_scan': user_scan
        }
        
    except:
        return Exception('Error while getting basics kpis')