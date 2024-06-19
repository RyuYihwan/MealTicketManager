import json


class Restaurant:
    """
    식당 클래스
    """

    def __init__(self, restaurant_id: str, name: str, show_menu: int, menu):
        self.restaurant_id = restaurant_id
        self.name = name
        self.show_menu = show_menu
        self.menu = menu


class RestaurantDataAccess:
    """
    식당 데이터 접근 클래스
    """

    def __init__(self, data_path):
        self.__data_path = data_path

    def get_restaurants(self):
        with open(self.__data_path, 'r', encoding='utf-8') as f:
            restaurants = json.load(f).get('restaurant')
            return restaurants

    def get_restaurant_by_id(self, restaurant_id):
        with open(self.__data_path, 'r', encoding='utf-8') as f:
            restaurants = self.get_restaurants()
            for restaurant in restaurants:
                if restaurant['restaurant_id'] == restaurant_id:
                    return restaurant

    def get_foods_by_id_and_time_settings(self, restaurant_id, meal_time):
        with open(self.__data_path, 'r', encoding='utf-8') as f:
            restaurants = self.get_restaurants()
            for dict_restaurant in restaurants:
                if dict_restaurant['restaurant_id'] == restaurant_id:
                    return dict_restaurant['menu'][meal_time]
