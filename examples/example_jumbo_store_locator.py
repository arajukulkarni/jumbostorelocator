from pprint import pprint

import requests

# -------------- Post coordinates and address  ----------------

url = 'http://localhost:5000/stores/findnearest'
payload = {
    "postal_address": "Stationsplein, 1012 AB Amsterdam",
    "coordinates": "52.3775763, 4.90138121396174"
}
headers = {
    "Content-Type": "application/json"
}
response = requests.post(url, json=payload, headers=headers)

# Get closest stores
if response.status_code == 200:
    result = response.json().get('closest_stores')
    pprint(result)
else:
    print('Request failed with status code:', response.status_code)
