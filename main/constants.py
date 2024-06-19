from enum import Enum

INITIAL_MESSAGE = \
    """
안녕하세요! 법틀 식권대장 프로그램입니다. 원하시는 기능의 번호를 선택해주세요.
1. 로그인
2. 회원가입
3. 프로그램 종료
"""

MANAGER_MODE_MESSAGE = \
    """
관리자 모드입니다. 원하시는 기능의 번호를 선택해주세요.
1. 아침/점심/저녁 시간 설정 변경
2. 식당 추가
"""

DEVELOPMENT_NOT_COMPLETED_MESSAGE = \
    """
죄송합니다. 아직 제공하지 않는 서비스입니다. 
"""

CHANGE_TIME_MENU_MESSAGE = \
    """
변경을 원하는 시간대의 번호를 선택 해주세요
1. 아침 식사 시간
2. 점심 식사 시간
3. 저녁 식사 시간
"""

INPUT_CHANGE_TIME_MESSAGE = \
    """
시간 형식은 시간:분 형태로 입력해 주세요. ex> 17:20
시간 설정 완료 후 프로그램이 재시작 됩니다.
"""

NOT_ORDER_RETURN_MAIN_MENU = \
    """
주문 취소 하셨습니다. 다시 시도해주세요.
"""


class Select(Enum):
    SIGN_IN = '1'
    SIGN_UP = '2'
    EXIT_PROGRAM = '3'


class SelectManagerMode(Enum):
    MEAL_TIME_SETTING = '1'
    ADD_RESTAURANT = '2'


class SelectTime(Enum):
    BREAKFAST_TIME = '1'
    LUNCH_TIME = '2'
    DINNER_TIME = '3'


class OrderResponse(Enum):
    YES = '1'
    NO = '2'
