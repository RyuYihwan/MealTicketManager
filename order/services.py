from datetime import datetime

from order.data_access import OrderDataAccess
from order.models import Order


class OrderService:
    def __init__(self, data_access: OrderDataAccess):
        self.__data_access = data_access

    # 주문
    def add_order(self, ordered_price, food_name, account_id, restaurant_id, food_id):
        orders = self.__data_access.get_orders()

        # id 부여
        order_id = 1
        if orders:
            order_id = orders[-1].get('order_id') + 1

        ordered_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        new_order = Order(order_id, ordered_time, ordered_price, food_name, account_id, restaurant_id, food_id)
        self.__data_access.add_order(new_order)

    # 임시 전체 주문 조회
    def get_orders(self):
        return self.__data_access.get_orders()
