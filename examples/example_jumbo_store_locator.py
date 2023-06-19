import requests


""" To run this example, make sure you start the web service by opening the file start_web_services and running it"""

# --------------- Get all stores  ----------------

url = 'http://localhost:5000/stores'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data[0])
else:
    print('Request failed with status code:', response.status_code)

# -------------- Post address only ----------------


url = 'http://localhost:5000/stores/findnearest'
payload = {
    "postal_address": "citerstraat 3c, 2287ep, rijswijk"
}
headers = {
    "Content-Type": "application/json"
}
response = requests.post(url, json=payload, headers=headers)

# Get closest stores
if response.status_code == 200:
    result = response.json().get('closest_stores')
    print("closest_stores:", result)
else:
    print('Request failed with status code:', response.status_code)


# -------------- Post coordinates only  ----------------
url = 'http://localhost:5000/stores/findnearest'
payload = {
    "coordinates": "52.3775763, 4.90138121396174"
}
headers = {
    "Content-Type": "application/json"
}
response = requests.post(url, json=payload, headers=headers)

# Get closest stores
if response.status_code == 200:
    result = response.json().get('closest_stores')
    print("closest_stores:", result)
else:
    print('Request failed with status code:', response.status_code)


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
    print("closest_stores:", result)
else:
    print('Request failed with status code:', response.status_code)