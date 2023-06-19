from pprint import pprint

import requests


""" To run this example, make sure you start the web service by opening the file start_web_services and running it"""

# --------------- Get all stores  ----------------

url = 'http://localhost:5000/stores'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    pprint(data[0])
else:
    print('Request failed with status code:', response.status_code)