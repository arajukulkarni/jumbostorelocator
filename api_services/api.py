from flask import Flask, jsonify, request

from store_locator.store_finder import StoreLocator, get_store_data

app = Flask(__name__)

# Sample data

store_data = get_store_data()


# GET /stores - Retrieve all stores
@app.route('/stores', methods=['GET'])
def get_stores():
    """
    Returns a jsonified dictionary of all stores in the database
    :return: dict
    """
    return jsonify(store_data)


# GET /stores/<id> - Retrieve a specific store
@app.route('/stores/<string:store_id>', methods=['GET'])
def get_book(store_id):
    """
    Returns the store in the database that corresponds to the given uuid
    :param store_id: should be a uuid of the store
    :return: dict
    """
    store = next((store for store in store_data if store['uuid'] == store_id), None)
    if store:
        return jsonify(store)
    return jsonify({"message": "Store not found"}), 404


@app.route('/stores/findnearest', methods=['POST'])
def findnearest():
    """
    Returns five closest stores to a given postal address or coordinates provided as an input by the api
    :return: dict
    """
    data = request.get_json()
    postal_address = data.get('postal_address', None)
    coordinates = data.get('coordinates', None)
    closest_stores = StoreLocator(postal_address=postal_address,
                                  coordinates=coordinates,
                                  store_data=store_data).generate_dictionary_five_closest_stores()
    return jsonify(closest_stores)


if __name__ == '__main__':
    app.run(debug=False, port=5000)
