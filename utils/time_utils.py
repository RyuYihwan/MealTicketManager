import json
from datetime import datetime


class TimeUtils:
    BREAKFAST_TIME_START = "7"
    BREAKFAST_TIME_END = "9",
    LUNCH_TIME_START = "11",
    LUNCH_TIME_END = "13",
    DINNER_TIME_START = "18",
    DINNER_TIME_END = "19"

    @staticmethod
    def get_current_time():
        return datetime.now().strftime("%H:%M:%S")

    @staticmethod
    def get_current_meal_time_settings():
        with open('./data/meal_time.json', 'r') as file:
            return json.load(file)

    @staticmethod
    def set_meal_time_settings():
        with open('./data/meal_time.json', 'w') as file:
            pass