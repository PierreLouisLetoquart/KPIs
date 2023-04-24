import json

def filter(data):

    # créer un dictionnaire pour stocker les informations du client
    customer_info = {}
    customer = data["order_created"]["customer"]
    customer_info["id"] = customer["id"]
    customer_info["email"] = customer["email"]
    customer_info["first_name"] = customer["first_name"]
    customer_info["last_name"] = customer["last_name"]
    customer_info["phone"] = customer["default_address"]["phone"]
    customer_info["address"] = customer["default_address"]["address1"]
    customer_info["city"] = customer["default_address"]["city"]
    customer_info["country"] = customer["default_address"]["country"]

    # créer un dictionnaire pour stocker les informations de l'article
    line_item_info = {}
    line_item = data["line_items"][0]
    line_item_info["id"] = line_item["id"]
    line_item_info["name"] = line_item["name"]
    line_item_info["quantity"] = line_item["quantity"]
    line_item_info["price"] = line_item["price"]
    line_item_info["tax_rate"] = line_item["tax_lines"][0]["rate"]
    line_item_info["tax_amount"] = line_item["tax_lines"][0]["price"]

    # créer un dictionnaire pour stocker les informations de la commande
    order_info = {}
    order_info["id"] = data["order_created"]["id"]
    order_info["name"] = data["order_created"]["name"]
    order_info["customer"] = customer_info
    order_info["line_item"] = line_item_info
    order_info["total_price"] = data["order_created"]["total_price"]
    order_info["total_tax"] = data["order_created"]["total_tax"]
    order_info["tags"] = data["order_created"]["tags"]
    order_info["order_number"] = data["order_created"]["order_number"]

    # retourner l'objet JSON de sortie
    output_json = json.dumps({"order_created": order_info})
    return output_json
