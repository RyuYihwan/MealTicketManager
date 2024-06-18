class AccountTemplate:

    def sign_in(self):
        print('로그인 화면 입니다.')
        return {
            'username': input('아이디: '),
            'password': input('비밀번호: ')
        }

    def sign_up(self):
        print('회원 가입 화면 입니다.')
        return {
            'username': input('아이디: '),
            'password': input('비밀번호: ')
        }

    def console_message(self, msg):
        print(msg)
