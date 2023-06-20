from pprint import pprint

import requests


""" To run this example, make sure you start the web service by opening the file start_web_services and running it"""


# -------------- Post address only ----------------


url = 'http://localhost:5000/stores/findnearest'
payload = {
    "postal_address": "Rijksweg 15 5462 CE Veghel"
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





