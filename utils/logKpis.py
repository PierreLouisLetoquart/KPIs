def count_total_records(filename):
    """Compte le nombre total d'enregistrements dans le fichier spécifié.

    Args:
        filename (str): Nom du fichier à traiter.

    Returns:
        int: Le nombre total d'enregistrements dans le fichier.

    """
    try:
        with open(filename, 'r') as f:
            return sum(1 for _ in f)
    except FileNotFoundError:
        print(f"{filename} not found.")
        return 0
    
def count_records_by_type(filename):
    """
    Retourne un dictionnaire avec le nombre d'enregistrements par type d'action
    du fichier csv spécifié.

    Args:
        filename (str): Le nom du fichier csv.

    Returns:
        dict: Un dictionnaire avec le nombre d'enregistrements par type d'action.

    """
    try:
        with open(filename, 'r') as f:
            next(f)
            records_by_type = {}
            for line in f:
                record = line.strip().split(',')
                if record[2] in records_by_type:
                    records_by_type[record[2]] += 1
                else:
                    records_by_type[record[2]] = 1
            return records_by_type
    except FileNotFoundError:
        print(f"{filename} not found.")
        return {}

import csv

def count_records_by_organization(filename):
    """
    Compte le nombre d'enregistrements pour chaque organisation dans un fichier CSV.

    Args:
        filename (str): Le nom du fichier CSV à lire.

    Returns:
        dict: Un dictionnaire avec le nombre d'enregistrements pour chaque organisation.

    Raises:
        FileNotFoundError: Si le fichier spécifié n'existe pas.
    """
    try:
        with open(filename, 'r') as f:
            records_by_org = {}
            reader = csv.DictReader(f)
            for row in reader:
                if row['organization'] in records_by_org:
                    records_by_org[row['organization']] += 1
                else:
                    records_by_org[row['organization']] = 1
            return records_by_org
    except FileNotFoundError:
        print(f"{filename} not found.")
        return {}


from datetime import datetime

def count_records_by_date(filename):
    """
    Counts the number of records in a CSV file by date.

    Args:
    - filename (str): the name of the CSV file to read

    Returns:
    - A dictionary containing the number of records for each date in the format 'YYYY-MM-DD'

    Raises:
    - FileNotFoundError: if the file specified by `filename` does not exist
    """
    try:
        with open(filename, 'r') as f:
            next(f)  # skip header row
            records_by_date = {}
            for line in f:
                record = line.strip().split(',')
                date = datetime.fromisoformat(record[1][:19])
                date_str = date.strftime('%Y-%m-%d')
                if date_str in records_by_date:
                    records_by_date[date_str] += 1
                else:
                    records_by_date[date_str] = 1
            return records_by_date
    except FileNotFoundError:
        print(f"{filename} not found.")
        return {}


def count_distinct_types(filename):
    """
    Counts the distinct types in the given CSV file and returns them as a set.

    Args:
        filename (str): The name of the CSV file to read.

    Returns:
        set: A set of distinct types found in the CSV file.

    Raises:
        FileNotFoundError: If the given file does not exist.
    """
    try:
        with open(filename, 'r') as f:
            distinct_types = set()
            reader = csv.DictReader(f)
            for row in reader:
                if(row['type'] not in distinct_types):
                    distinct_types.add(row['type'])
            return distinct_types
    except FileNotFoundError:
        print(f"{filename} not found.")
        return 0
