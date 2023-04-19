import setup
from utils.kpisExtraction import count_distinct_types, count_records_by_date, count_records_by_organization, count_records_by_type, count_total_records

dataset = "data/logs.csv"

# Point d'entrée du programme
if __name__ == "__main__":
    print("Records by date:\n\n", count_distinct_types(dataset))
