import json

from restaurant.restaurant import Restaurant


class DataAccess:
    def __init__(self, data_path):
        self._data_path = data_path

    def get_restaurants(self):
        with open(self._data_path, 'r', encoding='utf-8') as f:
            restaurants = json.load(f).get('restaurant')
            return restaurants

    def get_restaurant_by_name(self, restaurant_name):
        with open(self._data_path, 'r', encoding='utf-8') as f:
            restaurants = self.get_restaurants()
            for dict_restaurant in restaurants:
                if dict_restaurant['name'] == restaurant_name:
                    restaurant = Restaurant(**dict_restaurant)
                    print(restaurant.__dict__)
                    return restaurant
