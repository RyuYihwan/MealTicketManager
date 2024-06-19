from datetime import datetime

from account.models import AccountDataAccess
from order.exceptions import OrderException
from order.models import Order, OrderDataAccess
from order.templates import OrderTemplate
from utils.decorators import exception_handler


class OrderView:
    def __init__(self, order_template: OrderTemplate, order_data_access: OrderDataAccess,
                 account_data_access: AccountDataAccess):
        self.__order_template = order_template
        self.__order_data_access = order_data_access
        self.__account_data_access = account_data_access

    # 주문
    @exception_handler
    def add_order(self, ordered_price, food_name, account_id, restaurant_id, food_id):
        orders = self.__order_data_access.get_orders()

        account_money = self.__account_data_access.get_account_money(account_id)

        if account_money < ordered_price:
            raise OrderException('잔액이 부족 합니다.')

        # id 부여
        order_id = 1
        if orders:
            order_id = orders[-1].get('order_id') + 1

        ordered_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        new_order = Order(order_id, ordered_time, ordered_price, food_name, account_id, restaurant_id, food_id)

        # 주문 등록
        self.__order_data_access.add_order(new_order)

        # 금액 차감
        self.__account_data_access.set_account_money(account_id, account_money - ordered_price)

        # 결과 출력
        self.__order_template.order_complete(new_order)

    @exception_handler
    def check_order(self, selected_menu):
        order_response = self.__order_template.check_order(selected_menu)
        return order_response

    # 임시 전체 주문 조회
    def get_orders(self):
        return self.__order_data_access.get_orders()
