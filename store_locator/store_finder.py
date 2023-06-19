from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import json

from GLOBS import STORE_DATA_FILE


def get_store_data():
    with open(STORE_DATA_FILE) as f:
        store_data = json.load(f)
    return store_data['stores']


class StoreLocator(object):
    """
    This class is used to locate five closest stores to a given postal address or its coordinate
    """

    def __init__(self, postal_address=None, coordinates=None, store_data=None):
        """
        This class takes the optional inputs of postal address and/or location coordinates and defines the variables
        not provided by the user. If both postal address and coordinates are provided, an error is raised.

        Store data is the data of all stores saved in the json file. This can be read once again or provided as an
        input.
        :param postal_address: str
        :param coordinates: str
        :param store_data: dict
        """

        if not store_data:
            self.store_data = get_store_data()
        else:
            self.store_data = store_data

        if not postal_address and not coordinates:
            raise ValueError(self.input_error)

        if postal_address:
            self.postal_address = postal_address
            try:
                self.coordinates = self.get_coordinates()
            except ValueError:
                raise ValueError(self.input_error)

        if coordinates:
            try:
                self.coordinates = [float(a) for a in coordinates.split(',')]
            except ValueError:
                raise ValueError(self.input_error)

    input_error = ("Please provide correct address or coordinates of your location in string format.\n "
                     "E.g. address='Stationsplein, 1012 AB Amsterdam' or coordinates='52.3775763, 4.90138121396174'.")

    def get_coordinates(self):
        """
        Uses the postal address to determine the coordinates of the location [latitude, longitude]
        :return: list
        """
        geolocator = Nominatim(user_agent="my_geocoder")
        location_data = geolocator.geocode(self.postal_address)
        return [location_data.latitude, location_data.longitude]

    def get_distance_from_all_stores(self):
        """
        Gives the distance from the input postal address/coordinate in km for each store in the database

        :return: list
        """
        coordinates = self.coordinates
        distances = [geodesic(coordinates, (store['latitude'], store['longitude'])).km
                     for store in self.store_data]
        return distances

    def get_five_closest_store_indices(self):
        """
        Returns the indices of stores with five lowest distances from the list of distances generated in
        get_distance_from_all_stores()
        :return: list
        """
        distances = self.get_distance_from_all_stores()
        res = sorted(range(len(distances)), key=lambda sub: distances[sub])[:5]
        return res

    def generate_dictionary_five_closest_stores(self):
        """
        Generates a dictionary of five closest stores to input postal address or coordinates
        :return: dict
        """
        indices = self.get_five_closest_store_indices()
        closest_stores = [self.store_data[i] for i in indices]
        dictionary = {'closest_stores': closest_stores}
        return dictionary


if __name__ == '__main__':
    address = "Stationsplein, 1012 AB Amsterdam"
    obj = StoreLocator(postal_address=address)
    obj.generate_dictionary_five_closest_stores()
