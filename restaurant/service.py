from restaurant.data_access import DataAccess


class Service:
    def __init__(self, data_access: DataAccess):
        self.data_access = data_access

    # 조회
    def get_restaurants(self):
        return self.data_access.get_restaurants()
