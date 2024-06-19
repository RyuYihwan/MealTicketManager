# 싱글톤 객체 주입 관리
from account.models import AccountDataAccess
from account.templates import AccountTemplate
from account.views import AccountView
from main.main import MainService
from main.templates import MainTemplate
from order.models import OrderDataAccess
from order.templates import OrderTemplate
from order.views import OrderView
from restaurant.models import RestaurantDataAccess
from restaurant.templates import RestaurantTemplate
from restaurant.views import RestaurantView
from utils.decorators import singleton_handler


@singleton_handler
class AppConfig:
    def __init__(self):
        self.__initialize()

    def __initialize(self):
        self.account_data_access = AccountDataAccess('db/account.json')
        self.account_template = AccountTemplate()
        self.account_view = AccountView(self.account_template, self.account_data_access)

        self.restaurant_data_access = RestaurantDataAccess('db/restaurant.json')
        self.restaurant_template = RestaurantTemplate()
        self.restaurant_view = RestaurantView(self.restaurant_template, self.restaurant_data_access)

        self.order_data_access = OrderDataAccess('db/order.json')
        self.order_template = OrderTemplate()
        self.order_view = OrderView(self.order_template, self.order_data_access, self.account_data_access)

        self.main_template = MainTemplate()

    def get_main_service(self):
        return MainService(self.main_template, self.account_view, self.restaurant_view, self.order_view)