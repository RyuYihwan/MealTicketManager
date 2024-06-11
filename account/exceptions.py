class AccountNotFound(Exception):
    def __str__(self):
        return "Account Not Found"


class PasswordNotMatched(Exception):
    def __str__(self):
        return "Account Not Found"
