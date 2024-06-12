import json


class DataAccess:
    def __init__(self, data_path):
        self._data_path = data_path

    def get_restaurants(self):
        with open(self._data_path, 'r', encoding='utf-8') as f:
            restaurants = json.load(f).get('restaurant')
            return restaurants
