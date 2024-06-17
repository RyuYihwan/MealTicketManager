class AccountTemplate:

    def sign_in(self):
        return {
            'username': input('아이디: '),
            'password': input('비밀번호: ')
        }

    def sign_up(self):
        return {
            'username': input('아이디: '),
            'password': input('비밀번호: ')
        }

    def console_message(self, msg):
        print(msg)
