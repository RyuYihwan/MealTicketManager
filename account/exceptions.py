class AccountNotFound(Exception):
    def __str__(self):
        return "없는 아이디입니다."


class PasswordNotMatched(Exception):
    def __str__(self):
        return "다시 로그인 해주세요."


class AccountExisted(Exception):

    def __str__(self):
        return "이미 있는 아이디입니다."
