from main_service.main_service import MainService


def run():
    main = MainService()
    main.ticket_logic()


if __name__ == '__main__':
    run()
