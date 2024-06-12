class Account:
    """
    계정 클래스
    """
    def __init__(self, account_id: str, username: str, password: str, role: int):
        self.account_id = account_id
        self.username = username
        self.password = password
        # Enum value 로 생성
        self.role = role
