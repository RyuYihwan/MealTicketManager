import json
from datetime import datetime

from main.constants import SelectTime
from utils.exceptions import UtilException
from utils.decorators import exception_handler

class TimeUtils:
    BREAKFAST_TIME_START = ""
    BREAKFAST_TIME_END = ""
    LUNCH_TIME_START = ""
    LUNCH_TIME_END = ""
    DINNER_TIME_START = ""
    DINNER_TIME_END = ""

    @staticmethod
    def get_current_time():
        return datetime.now().strftime("%H:%M")

    @classmethod
    def get_current_meal_time_settings(cls):
        with open('./db/meal_time.json', 'r') as f:
            meal_time_settings = json.load(f)
            cls.BREAKFAST_TIME_START = meal_time_settings['BREAKFAST_TIME_START']
            cls.BREAKFAST_TIME_END = meal_time_settings['BREAKFAST_TIME_END']
            cls.LUNCH_TIME_START = meal_time_settings['LUNCH_TIME_START']
            cls.LUNCH_TIME_END = meal_time_settings['LUNCH_TIME_END']
            cls.DINNER_TIME_START = meal_time_settings['DINNER_TIME_START']
            cls.DINNER_TIME_END = meal_time_settings['DINNER_TIME_END']

    @classmethod
    def print_current_meal_time_settings(cls):
        print('설정된 시간 입니다.')
        print(f'BREAKFAST_TIME_START: {cls.BREAKFAST_TIME_START}')
        print(f'BREAKFAST_TIME_END: {cls.BREAKFAST_TIME_END}')
        print(f'LUNCH_TIME_START: {cls.LUNCH_TIME_START}')
        print(f'LUNCH_TIME_END: {cls.LUNCH_TIME_END}')
        print(f'DINNER_TIME_START: {cls.DINNER_TIME_START}')
        print(f'DINNER_TIME_END: {cls.DINNER_TIME_END}')

    @classmethod
    @exception_handler
    def get_meal_time_from_settings(cls):
        current_time = datetime.now().time()
        breakfast_time_start = datetime.strptime(cls.BREAKFAST_TIME_START, "%H:%M").time()
        breakfast_time_end = datetime.strptime(cls.BREAKFAST_TIME_END, "%H:%M").time()
        lunch_time_start = datetime.strptime(cls.LUNCH_TIME_START, "%H:%M").time()
        lunch_time_end = datetime.strptime(cls.LUNCH_TIME_END, "%H:%M").time()
        dinner_time_start = datetime.strptime(cls.DINNER_TIME_START, "%H:%M").time()
        dinner_time_end = datetime.strptime(cls.DINNER_TIME_END, "%H:%M").time()

        if breakfast_time_start <= current_time <= breakfast_time_end:
            return 'breakfast'
        elif lunch_time_start <= current_time <= lunch_time_end:
            return 'lunch'
        elif dinner_time_start <= current_time <= dinner_time_end:
            return 'dinner'
        else:
            raise UtilException('현재는 운영 시간이 아닙니다. 관리자에게 문의해주세요.')

    @classmethod
    def set_meal_time_setting(cls, select_time, start_time, end_time):
        with open('./db/meal_time.json', 'w') as f:

            if select_time == SelectTime.BREAKFAST_TIME:
                cls.BREAKFAST_TIME_START = start_time
                cls.BREAKFAST_TIME_END = end_time
            elif select_time == SelectTime.LUNCH_TIME:
                cls.LUNCH_TIME_START = start_time
                cls.LUNCH_TIME_END = end_time
            elif select_time == SelectTime.DINNER_TIME:
                cls.DINNER_TIME_START = start_time
                cls.DINNER_TIME_END = end_time

            meal_time_settings = {'BREAKFAST_TIME_START': cls.BREAKFAST_TIME_START,
                                  'BREAKFAST_TIME_END': cls.BREAKFAST_TIME_END,
                                  'LUNCH_TIME_START': cls.LUNCH_TIME_START,
                                  'LUNCH_TIME_END': cls.LUNCH_TIME_END,
                                  'DINNER_TIME_START': cls.DINNER_TIME_START,
                                  'DINNER_TIME_END': cls.DINNER_TIME_END}
            json.dump(meal_time_settings, f, indent=4)
