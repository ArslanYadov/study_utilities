import logging

def check_status(func):
    """Проверка статуса ответа."""
    def wrapper(*args, **kwargs):
        response = func(*args, **kwargs)
        return response.status_code
    return wrapper


@check_status
def site(url: str):
    """GET запрос сайта."""
    import requests
    return requests.get(url)


def get_url() -> str:
    """Запросить url у пользователя."""
    url: str = input('Введите адрес для проверки: ')
    url = 'https://' + url + '/'
    return url


def show_info(url: str, code: int) -> str:
    """Вывод информации."""
    return 'Сайт: {}; Код ответа: {}'.format(url, code)


def main():
    url: str = get_url()
    while True:
        try:
            code: int = site(url)
            break
        except Exception as ex:
            logging.error(ex)
            url = get_url()
    print(show_info(url, code))


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format='[%(levelname)s] : %(message)s'
    )
    main()
