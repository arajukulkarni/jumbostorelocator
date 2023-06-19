import unittest

from store_locator.store_finder import StoreLocator


class StoreLocatorTest(unittest.TestCase):
    def test_find_closest(self):
        address = "Stationsplein, 1012 AB Amsterdam"
        locator = StoreLocator(postal_address=address)
        result = locator.generate_dictionary_five_closest_stores()
        model_result = {'closest_stores': [
            {'addressName': 'Jumbo Amsterdam Westerstraat', 'city': 'Amsterdam', 'collectionPoint': True,
             'complexNumber': '30644', 'latitude': '52.378670', 'locationType': 'SupermarktPuP',
             'longitude': '4.883832', 'postalCode': '1015 MN', 'sapStoreID': '6364', 'showWarningMessage': True,
             'street': 'Westerstraat', 'street2': '98-102', 'street3': '', 'todayClose': '21:00', 'todayOpen': '08:00',
             'uuid': 'R74KYx4XucoAAAFIqY8YwKxK'},
            {'addressName': 'Jumbo Amsterdam Foodmarkt Amsterdam', 'city': 'Amsterdam', 'complexNumber': '32205',
             'latitude': '52.383263', 'locationType': 'Supermarkt', 'longitude': '4.919767', 'postalCode': '1021 KP',
             'sapStoreID': '4703', 'showWarningMessage': True, 'street': 'Gedempt Hamerkanaal', 'street2': '223',
             'street3': '', 'todayClose': '21:00', 'todayOpen': '08:00', 'uuid': '5KsKYx4XUj8AAAFJ7S5Gp2Rc'},
            {'addressName': 'Jumbo Amsterdam Spaarndammerstraat', 'city': 'Amsterdam', 'complexNumber': '32252',
             'latitude': '52.389402', 'locationType': 'Supermarkt', 'longitude': '4.879655', 'postalCode': '1013 TH',
             'sapStoreID': '4726', 'showWarningMessage': True, 'street': 'Spaarndammerstraat', 'street2': '544',
             'street3': '', 'todayClose': '22:00', 'todayOpen': '08:00', 'uuid': 'qisKYx4X6wwAAAFY.DNSOmWN'},
            {'addressName': 'Jumbo Amsterdam Stadhouderskade', 'city': 'Amsterdam', 'complexNumber': '32266',
             'latitude': '52.357579', 'locationType': 'Supermarkt', 'longitude': '4.895801', 'postalCode': '1073 AV',
             'sapStoreID': '4738', 'showWarningMessage': True, 'street': 'Stadhouderskade', 'street2': '93',
             'street3': '', 'todayClose': '22:00', 'todayOpen': '08:00', 'uuid': 'dhkKYx4XS0UAAAFcnMNlwJ7N'},
            {'addressName': 'Jumbo Amsterdam Oostelijke Handelskade', 'city': 'Amsterdam', 'collectionPoint': True,
             'complexNumber': '33023', 'latitude': '52.374447', 'locationType': 'SupermarktPuP',
             'longitude': '4.935351', 'postalCode': '1019 BW', 'sapStoreID': '3427', 'showWarningMessage': True,
             'street': 'Oostelijke Handelskade', 'street2': '1005', 'street3': '', 'todayClose': '22:00',
             'todayOpen': '08:00', 'uuid': 'bBkKYx4XaBwAAAFNDfk7fpNP'}]}

        self.assertEqual(result, model_result)


if __name__ == '__main__':
    unittest.main()
