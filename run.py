from main.app import MainService


def run():
    main = MainService()
    main.ticket_logic()


if __name__ == '__main__':
    run()
