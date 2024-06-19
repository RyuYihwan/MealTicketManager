from restaurant.models import RestaurantDataAccess
from restaurant.templates import RestaurantTemplate


class RestaurantView:
    def __init__(self, restaurant_template: RestaurantTemplate, restaurant_data_access: RestaurantDataAccess):
        self.__restaurant_template = restaurant_template
        self.__restaurant_data_access = restaurant_data_access

    # 식당 선택
    def choose_restaurant(self, meal_time):
        restaurants = self.__restaurant_data_access.get_restaurants()

        selected_restaurant_id = self.__restaurant_template.choose_restaurant(restaurants, meal_time)

        return int(selected_restaurant_id)

    def choose_menu(self, selected_restaurant_id, meal_time):
        restaurant = self.__restaurant_data_access.get_restaurant_by_id(selected_restaurant_id)

        selected_menu = self.__restaurant_template.choose_menu(restaurant, meal_time)

        return selected_menu
