import requests
import json

data = []
for year in (2000, 2099):

    url = f"https://feiertage-api.de/api/?jahr={year}"
    data.append(requests.get(url).json())

with open('data.json', 'w') as f:
    json.dump(data, f)
