import json
import uuid


class Order:
    """
    주문 데이터 클래스
    """

    def __init__(self, order_id: str, ordered_time: str, ordered_price: int, food_name: str, account_id,
                 restaurant_id: int, food_id: int):
        self.order_id = order_id
        self.ordered_time = ordered_time
        self.ordered_price = ordered_price
        self.food_name = food_name
        self.account_id = account_id
        self.restaurant_id = restaurant_id
        self.food_id = food_id


class OrderDataAccess:
    """
    주문 데이터 접근 클래스
    """

    def __init__(self, data_path):
        self.__data_path = data_path

    def get_orders(self):
        with open(self.__data_path, 'r', encoding='utf-8') as f:
            orders = json.load(f).get('order')
            return orders

    # 일단 임시 데이터이므로 불러오고 덮어 쓰기 형태로 진행함.
    # json 형태로 이어쓸 정도로 필요 하지 않음.
    def add_order(self, order):
        orders = self.get_orders()
        json_order = order.__dict__
        orders.append(json_order)
        with open(self.__data_path, 'w', encoding='utf-8') as f:
            json.dump({'order': orders}, f, ensure_ascii=False, indent=4)
