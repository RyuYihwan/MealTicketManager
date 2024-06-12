class AccountNotFound(Exception):
    def __str__(self):
        return "없는 아이디입니다."


class PasswordNotMatched(Exception):
    def __str__(self):
        return "다시 로그인 해주세요."
