import json

def filter_order(input: json) -> json:
    """
    Filtre et renvoie un objet JSON contenant uniquement les informations
    pertinentes d'une commande.
    
    Args:
        input (json): un objet JSON contenant des informations de commande.
    
    Returns:
        json: un objet JSON contenant les informations filtrées de la commande.
    """
    try:
        order = input["order_created"]
    except (KeyError, TypeError):
        raise ValueError("Entrée invalide : l'objet JSON doit contenir une clé 'order_created'.")
        
    try:
        filtered_order = {}
        filtered_order["name"] = order["name"]
        filtered_order["id"] = order["id"]
        filtered_order["order_number"] = order["order_number"]
        filtered_order["total_price"] = order["total_price"]
        filtered_order["total_tax"] = order["total_tax"]
        filtered_order["customer"] = order["customer"]
        filtered_order["line_items"] = order["line_items"]
        filtered_order["tags"] = order["tags"]
    except KeyError as e:
        raise ValueError(f"Entrée invalide : la clé {str(e)} est manquante dans l'objet JSON.")
    except TypeError:
        raise ValueError("Entrée invalide : l'objet JSON doit être un dictionnaire.")

    try:
        return json.dumps(filtered_order, sort_keys=True)
    except TypeError:
        raise ValueError("La conversion en JSON a échoué : l'objet filtré contient des données non-JSON.")

def filter_logs(input: json) -> json:
    """
    Filtre et renvoie un objet JSON contenant uniquement les informations
    pertinentes d'un journal d'activité.
    
    Args:
        input (json): un objet JSON contenant des informations de journal d'activité.
    
    Returns:
        json: un objet JSON contenant les informations filtrées du journal d'activité.
    """
    try:
        data = input["data"]
        headers = input["headers"]
    except (KeyError, TypeError):
        raise ValueError("Entrée invalide : l'objet JSON doit contenir une clé 'data' et 'headers'.")
    
    try:
        filtered_data = {}
        filtered_data["fid"] = data["fid"]
        filtered_data["options"] = data["options"]
        filtered_variants = []
        for variant in data["variants"]:
            filtered_variant = {}
            filtered_variant["id"] = variant["id"]
            filtered_variant["name"] = variant["name"]
            filtered_variant["sku"] = variant["sku"]
            filtered_variant["title"] = variant["title"]
            filtered_variant["options"] = variant["options"]
            filtered_variant["available"] = variant["available"]
            filtered_variant["compare_at_price"] = variant["compare_at_price"]
            filtered_variants.append(filtered_variant)
        filtered_data["variants"] = filtered_variants
        
        filtered_headers = {}
        filtered_headers["origin"] = headers["origin"]  
        filtered_headers["x-real-ip"] = headers["x-real-ip"]
        if "x-vercel-ip-country" in headers:
            filtered_headers["x-vercel-ip-country"] = headers["x-vercel-ip-country"]
        if "x-vercel-ip-city" in headers:
            filtered_headers["x-vercel-ip-city"] = headers["x-vercel-ip-city"]

        filtered_log = {}
        filtered_log["data"] = filtered_data
        filtered_log["headers"] = filtered_headers
    except KeyError as e:
        raise ValueError(f"Entrée invalide : la clé {str(e)} est manquante dans l'objet JSON.")
    except TypeError:
        raise ValueError("Entrée invalide : l'objet JSON doit être un dictionnaire.")
    
    try:
        return json.dumps(filtered_log, sort_keys=True)
    except TypeError:
        raise ValueError("La conversion en JSON a échoué : l'objet filtré contient des données non-JSON.")
    
def load_json_file(filename: str) -> dict:
    """
    Charge le contenu d'un fichier JSON dans un dictionnaire Python.
    
    Args:
        filename (str): Le nom de fichier à lire.
    
    Returns:
        dict: Le contenu du fichier JSON sous forme de dictionnaire Python.
    
    Raises:
        FileNotFoundError: Si le fichier spécifié n'existe pas.
        ValueError: Si le contenu du fichier n'est pas un objet JSON valide.
    """
    try:
        with open(filename, 'r') as f:
            json_data = json.load(f)
            if not isinstance(json_data, dict):
                raise ValueError("Le contenu du fichier doit être un objet JSON valide.")
            return json_data
    except FileNotFoundError:
        print(f"Le fichier '{filename}' n'existe pas.")
    except json.JSONDecodeError:
        print(f"Le contenu du fichier '{filename}' n'est pas un objet JSON valide.")

def save_json_file(json_data: dict, filename: str) -> None:
    """
    Enregistre un dictionnaire Python dans un fichier JSON avec un nom de fichier spécifié.
    
    Args:
        json_data (dict): Le dictionnaire Python à enregistrer dans le fichier JSON.
        filename (str): Le nom de fichier à écrire.
    
    Raises:
        TypeError: Si le contenu du dictionnaire n'est pas sérialisable en JSON.
    """
    try:
        with open(filename, 'w') as f:
            json.dump(json_data, f)
    except TypeError:
        print(f"Le contenu du dictionnaire n'est pas sérialisable en JSON.")
