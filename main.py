import json
from utils.jsonFilters import filter

# charger les données depuis le fichier JSON
with open("./in_sample.json", "r") as f:
    data = json.load(f)

# appliquer le filtre aux données chargées
result = filter(data)

# imprimer le résultat
print(result)