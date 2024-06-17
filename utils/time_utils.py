import json
from datetime import datetime


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
            return 'breaktime'

    @staticmethod
    def set_meal_time_settings(
            breakfast_time_start, breakfast_time_end,
            lunch_time_start, lunch_time_end,
            dinner_time_start, dinner_time_end,
    ):
        with open('./db/meal_time.json', 'w') as f:
            meal_time_settings = {'BREAKFAST_TIME_START': breakfast_time_start,
                                  'BREAKFAST_TIME_END': breakfast_time_end, 'LUNCH_TIME_START': lunch_time_start,
                                  'LUNCH_TIME_END': lunch_time_end, 'DINNER_TIME_START': dinner_time_start,
                                  'DINNER_TIME_END': dinner_time_end}
            json.dump(meal_time_settings, f, indent=4)
