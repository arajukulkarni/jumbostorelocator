import unittest
import requests


class StoreApiTest(unittest.TestCase):
    def test_get_stores(self):
        url = 'http://localhost:5000/stores'
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_one_store(self):
        url = 'http://localhost:5000/stores/O1YKYx4XAw8AAAFIdb8YwKxJ'
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)

    def test_find_store(self):
        url = 'http://localhost:5000/stores/findnearest'
        payload = {"postal_address": "citerstraat 3c, 2287ep, rijswijk" }
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, json=payload, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)


if __name__ == '__main__':
    unittest.main()
