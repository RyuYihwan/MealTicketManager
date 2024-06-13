import json

from restaurant.restaurant import Restaurant


class DataAccess:
    def __init__(self, data_path):
        self._data_path = data_path

    def get_restaurants(self):
        with open(self._data_path, 'r', encoding='utf-8') as f:
            restaurants = json.load(f).get('restaurant')
            return restaurants

    def get_restaurant_by_id(self, restaurant_id):
        with open(self._data_path, 'r', encoding='utf-8') as f:
            restaurants = self.get_restaurants()
            for dict_restaurant in restaurants:
                if dict_restaurant['restaurant_id'] == restaurant_id:
                    restaurant = Restaurant(**dict_restaurant)
                    print(restaurant.__dict__)
                    return restaurant

    def get_foods_by_id_and_time_settings(self, restaurant_id, meal_time):
        with open(self._data_path, 'r', encoding='utf-8') as f:
            restaurants = self.get_restaurants()
            for dict_restaurant in restaurants:
                if dict_restaurant['restaurant_id'] == restaurant_id:
                    return dict_restaurant['menu'][meal_time]
