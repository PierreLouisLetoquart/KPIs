import os
from utils.supabaseClient import create_supabase_client
from utils.supabaseDataloader import fetch_logs, fetch_orders, store_data_to_csv

def console_clear():
    # Effacer la console sur Windows
    if os.name == "nt":
        os.system("cls")
    # Effacer la console sur Linux et macOS
    else:
        os.system("clear")

# Fonction pour afficher le sous-menu "Extract Data"
def extract_data_menu():
    while True:
        console_clear()
        print("\n--- Extraction de données ---")
        print("1. Logs")
        print("2. Orders")
        print("3. O join l")
        print("4. Retour au menu principal")
        choice = input("Entrez votre choix : ")
        
        if choice == "1":
            try:
                organization_name = input("Entrez le nom de l'organisation : ")
                supabase_client = create_supabase_client()
                logs_df = fetch_logs(supabase_client, organization=organization_name)
                store_data_to_csv(logs_df, "./extract_KPIs/tests/logs.csv")
                print("Données extraites avec succès !")
            except:
                print("Erreur lors de l'extraction des données.")
        elif choice == "2":
            try:
                organization_id = input("Entrez l'ID de l'organisation : ")
                supabase_client = create_supabase_client()
                orders_df = fetch_orders(supabase_client, organization_id=organization_id)
                store_data_to_csv(orders_df, "./extract_KPIs/tests/orders.csv")
                print("Données extraites avec succès !")
            except:
                print("Erreur lors de l'extraction des données.")
        elif choice == "3":
            print("Développement en cours...")
        elif choice == "4":
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

# Fonction pour afficher le menu principal
def main_menu():
    while True:
        console_clear()
        print("\n--- Menu principal ---")
        print("1. Extraction de données")
        print("2. Autre section")
        print("3. Quitter")
        choice = input("Entrez votre choix : ")
        
        # Utilisation d'un switch pour facilement ajouter d'autres sections dans le futur
        if choice == "1":
            extract_data_menu()
        elif choice == "2":
            print("Section en cours de développement...")
        elif choice == "3":
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")
