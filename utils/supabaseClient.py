import os
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
