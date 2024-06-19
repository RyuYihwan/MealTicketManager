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


def run():
    # 인스턴스 생성 -> 싱글톤 패턴으로 수정 필요함(AppConfig 통해서)
    account_data_access = AccountDataAccess('db/account.json')
    account_template = AccountTemplate()
    account_view = AccountView(account_template, account_data_access)

    restaurant_data_access = RestaurantDataAccess('db/restaurant.json')
    restaurant_template = RestaurantTemplate()
    restaurant_view = RestaurantView(restaurant_template, restaurant_data_access)

    order_data_access = OrderDataAccess('db/order.json')
    order_template = OrderTemplate()
    order_view = OrderView(order_template, order_data_access, account_data_access)

    main_template = MainTemplate()

    main = MainService(main_template, account_view, restaurant_view, order_view)
    main.ticket_logic()


if __name__ == '__main__':
    run()
