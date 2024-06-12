import json


class DataAccess:
    def __init__(self, data_path):
        self._data_path = data_path

    def get_restaurants(self):
        with open(self._data_path, 'r', encoding='utf-8') as f:
            restaurants = json.load(f).get('restaurant')
            return restaurants
    #
    # def add_account(self, account):
    #     accounts = self.get_accounts()
    #     json_account = account.__dict__
    #     accounts.append(json_account)
    #     with open(self._data_path, 'w') as f:
    #         json.dump({'account': accounts}, f)
    #
    # def find_restaurant_by_restaurant_name(self, restaurant_name):
    #     restaurants = self.get_restaurants()
    #     for dict_restaurant in restaurants:
    #         if dict_restaurant['name'] == restaurant_name:
    #             account = Account(**dict_account)
    #             print(account.__dict__)
    #             return account
