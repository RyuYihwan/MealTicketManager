from main.config import AppConfig


def run():

    app_config = AppConfig()

    main = app_config.get_main_service()

    main.ticket_logic()


if __name__ == '__main__':
    run()
