from account.constants import Roles
from account.views import AccountView
from main.constants import Select, SelectManagerMode, DEVELOPMENT_NOT_COMPLETED_MESSAGE, NOT_ORDER_RETURN_MAIN_MENU, \
    OrderResponse
from main.templates import MainTemplate
from order.views import OrderView
from restaurant.views import RestaurantView
from utils.time_utils import TimeUtils


class MainService:
    def __init__(self, main_template: MainTemplate, account_view: AccountView, restaurant_view: RestaurantView,
                 order_view: OrderView):
        self.__main_template = main_template
        self.__account_view = account_view
        self.__restaurant_view = restaurant_view
        self.__order_view = order_view

    def ticket_logic(self):
        # 설정 시간 초기화
        TimeUtils.get_current_meal_time_settings()

        # 선택 변수 선언 및 초기화
        select = -1

        # 종료 선택 전까지 반복
        while select != Select.EXIT_PROGRAM.value:

            # 메인 선택 화면
            select = self.__main_template.main_menu()

            # 로그인 선택
            if select == Select.SIGN_IN.value:

                # 로그인 계정 정보 유지
                account = self.__account_view.sign_in()

                # 계정이 예외로 인해 할당 되지 않으면 continue
                if account is None:
                    continue

                # 로그인 된 계정을 확인 후 역할에 따라 다른 모드 실행
                if account.role == Roles.MANAGER.value:

                    select_manager_mode = self.__main_template.manager_menu()

                    if select_manager_mode == SelectManagerMode.MEAL_TIME_SETTING.value:
                        # 현재 세팅된 시간을 출력 해주고 변경 시간을 입력 받도록 함 -> 재접속 필요
                        self.__set_meal_time_by_manager()

                    elif select_manager_mode == SelectManagerMode.ADD_RESTAURANT.value:
                        self.__main_template.information_message(DEVELOPMENT_NOT_COMPLETED_MESSAGE)

                elif account.role == Roles.NORMAL.value:

                    # 설정 시간과 현재 시간을 비교하여 시간대를 가져옴, 만약 운영시간이 아니라면 에러 메세지
                    meal_time = TimeUtils.get_meal_time_from_settings()

                    # 설정 시간이 예외로 인해 할당 되지 않으면 continue
                    if meal_time is None:
                        continue

                    # 식당 선택
                    selected_restaurant_id = self.__restaurant_view.choose_restaurant(meal_time)

                    # 메뉴 선택
                    selected_menu = self.__restaurant_view.choose_menu(selected_restaurant_id, meal_time)

                    # 주문 내용 및 의사 확인
                    order_response = self.__order_view.check_order(selected_menu)

                    # 주문
                    if order_response == OrderResponse.YES.value:
                        self.__order_view.add_order(int(selected_menu.get('food_price')), selected_menu.get('food_name'),
                                                    account.account_id, selected_restaurant_id,
                                                    selected_menu.get('food_id'))
                    else:
                        self.__main_template.information_message(NOT_ORDER_RETURN_MAIN_MENU)

            # 회원 가입 선택2
            elif select == Select.SIGN_UP.value:
                self.__account_view.sign_up()

    def __set_meal_time_by_manager(self):

        # 현재 세팅된 시간을 출력
        TimeUtils.print_current_meal_time_settings()

        # 변경을 원하는 시간대를 선택
        select_time = self.__main_template.change_time_menu()

        # 변경할 시간값 입력
        change_time_data = self.__main_template.input_change_time()

        # 시간 변경
        TimeUtils.set_meal_time_setting(select_time, change_time_data.get('start_time'),
                                        change_time_data.get('end_time'))

        # 변경한 시간값 토대로 다시 클래스 변수로 가져옴.
        TimeUtils.get_current_meal_time_settings()

        # 세팅된 시간을 전체 출력
        TimeUtils.print_current_meal_time_settings()
