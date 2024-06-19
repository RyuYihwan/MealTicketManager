from main.constants import INITIAL_MESSAGE, MANAGER_MODE_MESSAGE, CHANGE_TIME_MENU_MESSAGE, INPUT_CHANGE_TIME_MESSAGE


class MainTemplate:

    def main_menu(self):
        return input(INITIAL_MESSAGE)

    def manager_menu(self):
        return input(MANAGER_MODE_MESSAGE)

    def information_message(self, msg):
        print(msg)

    def change_time_menu(self):
        return input(CHANGE_TIME_MENU_MESSAGE)

    def input_change_time(self):
        print(INPUT_CHANGE_TIME_MESSAGE)
        return {
            'start_time': input("변경할 식사 시간의 시작 시간 입력: "),
            'end_time': input("변경할 식사 시간의 종료 시간 입력: ")
        }
