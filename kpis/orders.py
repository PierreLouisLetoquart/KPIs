from supabase import Client
import csv
import json
    
def count_total_orders(filename: str) -> int:
    """
    Compte le nombre total de commandes dans un fichier CSV.
    
    Args:
        filename (str): Nom du fichier CSV.
    
    Returns:
        int: Nombre total de commandes.
        
    Raises:
        FileNotFoundError: Si le fichier n'est pas trouvé.
    """
    try:
        with open(filename, 'r') as f:
            return len(f.readlines())
    except FileNotFoundError:
        print(f"{filename} not found.")
        return 0

def count_fringuant_orders(filename: str) -> int:
    """
    Compte le nombre de commandes effectuées grace à Fringuant dans un fichier CSV.
    
    Args:
        filename (str): Nom du fichier CSV.
    
    Returns:
        int: Nombre d'occurrences du mot 'fringuant' dans le fichier.
        
    Raises:
        FileNotFoundError: Si le fichier n'est pas trouvé.
    """
    try:
        with open(filename, 'r') as f:
            count = 0
            reader = csv.DictReader(f)
            for row in reader:
                if('fringuant' in row['data']):
                    count += 1
            return count
    except FileNotFoundError:
        print(f"{filename} not found.")
        return 0
