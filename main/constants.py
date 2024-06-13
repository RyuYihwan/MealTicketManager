from enum import Enum

INITIAL_MESSAGE = \
    """
안녕하세요! 법틀 식권대장 프로그램입니다. 원하시는 기능의 번호를 선택해주세요.
1. 로그인
2. 회원가입
3. 프로그램 종료
"""

AFTER_SIGN_IN_MESSAGE = \
    """
원하시는 식당을 선택해주세요. 
"""

SIGN_UP_MESSAGE = \
    """
일반 회원가입입니다. 사용하실 아이디와 비밀번호를 입력해주세요.
"""

MANAGER_MODE_MESSAGE = \
    """
관리자 모드입니다. 원하시는 기능의 번호를 선택해주세요.
1. 아침/점심/저녁 시간 설정 변경
2. 식당 추가
"""

NORMAL_MODE_MESSAGE = \
    """
주문할 식당을 선택해주세요.
일부 식당은 메뉴가 자동 선택됩니다.
"""

DEVELOPMENT_NOT_COMPLETED_MESSAGE = \
    """
죄송합니다. 아직 제공하지 않는 서비스입니다. 
"""


class Select(Enum):
    SIGN_IN = 1
    SIGN_UP = 2
    EXIT_PROGRAM = 3


class SelectManagerMode(Enum):
    MEAL_TIME_SETTING = 1
    ADD_RESTAURANT = 2
