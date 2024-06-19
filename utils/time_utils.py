import json
from datetime import datetime

from main.constants import SelectTime
from utils.decorators import exception_handler
from utils.exceptions import UtilException


class TimeUtils:
    BREAKFAST_TIME_START = ""
    BREAKFAST_TIME_END = ""
    LUNCH_TIME_START = ""
    LUNCH_TIME_END = ""
    DINNER_TIME_START = ""
    DINNER_TIME_END = ""

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
        breakfast_time_start = cls.convert_time(cls.BREAKFAST_TIME_START)
        breakfast_time_end = cls.convert_time(cls.BREAKFAST_TIME_END)
        lunch_time_start = cls.convert_time(cls.LUNCH_TIME_START)
        lunch_time_end = cls.convert_time(cls.LUNCH_TIME_END)
        dinner_time_start = cls.convert_time(cls.DINNER_TIME_START)
        dinner_time_end = cls.convert_time(cls.DINNER_TIME_END)

        if breakfast_time_start <= current_time <= breakfast_time_end:
            return 'breakfast'
        elif lunch_time_start <= current_time <= lunch_time_end:
            return 'lunch'
        elif dinner_time_start <= current_time <= dinner_time_end:
            return 'dinner'
        else:
            raise UtilException('현재는 운영 시간이 아닙니다. 관리자에게 문의해주세요.')

    @classmethod
    @exception_handler
    def set_meal_time_setting(cls, select_time, start_time, end_time):
        if select_time == SelectTime.BREAKFAST_TIME.value:
            if cls.convert_time(start_time) < cls.convert_time("04:00") or cls.convert_time(
                    end_time) > cls.convert_time("10:00"):
                raise UtilException('아침식사 시간은 04:00에서 10:00 사이에만 설정 가능합니다.')
            cls.BREAKFAST_TIME_START = start_time
            cls.BREAKFAST_TIME_END = end_time
        elif select_time == SelectTime.LUNCH_TIME.value:
            if cls.convert_time(start_time) < cls.convert_time("11:00") or cls.convert_time(
                    end_time) > cls.convert_time("15:00"):
                raise UtilException('점심식사 시간은 11:00에서 15:00 사이에만 설정 가능합니다.')
            cls.LUNCH_TIME_START = start_time
            cls.LUNCH_TIME_END = end_time
        elif select_time == SelectTime.DINNER_TIME.value:
            if cls.convert_time(start_time) < cls.convert_time("16:00") or cls.convert_time(
                    end_time) > cls.convert_time("23:59"):
                raise UtilException('저녁식사 시간은 16:00에서 23:59 사이에만 설정 가능합니다.')
            cls.DINNER_TIME_START = start_time
            cls.DINNER_TIME_END = end_time
        else:
            raise UtilException('입력값 오류입니다. 다시 시도 해주세요.')

        with open('./db/meal_time.json', 'w') as f:
            meal_time_settings = {'BREAKFAST_TIME_START': cls.BREAKFAST_TIME_START,
                                  'BREAKFAST_TIME_END': cls.BREAKFAST_TIME_END,
                                  'LUNCH_TIME_START': cls.LUNCH_TIME_START,
                                  'LUNCH_TIME_END': cls.LUNCH_TIME_END,
                                  'DINNER_TIME_START': cls.DINNER_TIME_START,
                                  'DINNER_TIME_END': cls.DINNER_TIME_END}
            json.dump(meal_time_settings, f, indent=4)

    @staticmethod
    def convert_time(str_time):
        return datetime.strptime(str_time, "%H:%M").time()

    @staticmethod
    def get_current_time():
        return datetime.now().strftime("%H:%M")
