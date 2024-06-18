from account.views import AccountView
from main.constants import Select
from main.templates import MainTemplate
from utils.time_utils import TimeUtils


class MainService:
    def __init__(self, main_template: MainTemplate, account_view: AccountView):
        self.__main_template = main_template
        self.__account_view = account_view

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
                self.__account_view.sign_in()

                # 로그인 된 계정을 확인 후 역할에 따라 다른 모드 실행

            # 회원 가입 선택
            elif select == Select.SIGN_UP.value:
                self.__account_view.sign_up()
