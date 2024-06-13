from datetime import datetime

from order.data_access import DataAccess
from order.order import Order


class Service:
    def __init__(self, data_access: DataAccess):
        self.data_access = data_access

    # 주문
    def add_order(self, ordered_price, food_name, account_id, restaurant_id, food_id):
        orders = self.data_access.get_orders()

        # id 부여
        order_id = 1
        if orders:
            order_id = orders[-1].get('account_id') + 1

        ordered_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        new_order = Order(order_id, ordered_time, ordered_price, food_name, account_id, restaurant_id, food_id)
        self.data_access.add_order(new_order)

    # 임시 전체 주문 조회
    def get_orders(self):
        return self.data_access.get_orders()
