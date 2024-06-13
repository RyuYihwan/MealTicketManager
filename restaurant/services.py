from restaurant.data_access import RestaurantDataAccess


class RestaurantService:
    def __init__(self, data_access: RestaurantDataAccess):
        self.data_access = data_access

    # 조회
    def get_restaurants(self):
        return self.data_access.get_restaurants()

    def get_restaurant_by_id(self, restaurant_id):
        return self.data_access.get_restaurant_by_id(restaurant_id)

    def get_foods_by_id_and_time_settings(self, restaurant_id, meal_time):
        return self.data_access.get_foods_by_id_and_time_settings(restaurant_id, meal_time)

