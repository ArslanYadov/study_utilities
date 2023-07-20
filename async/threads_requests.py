import asyncio
import requests
from concurrent.futures import ThreadPoolExecutor
from functools import partial

from async_decorators import async_timer
from conf import AMOUNT_REQUESTS


def get_response_status(url: str) -> int:
    """Получаем статус ответа."""
    return requests.get(url).status_code


@async_timer
async def main() -> None:
    """Множественные запросы к URL с помощью пула потоков."""
    # если использовать защищенный протокол https, то необходимо убрать
    # проверку сертификата SSL в requests.get(url, verify=False)
    requst_url: str = 'http://www.example.com'
    urls: list = [requst_url for _ in range(AMOUNT_REQUESTS)]
    with ThreadPoolExecutor(max_workers=AMOUNT_REQUESTS) as executor:
        loop = asyncio.get_running_loop()
        tasks: list = [
            loop.run_in_executor(executor, partial(get_response_status, url))
            for url in urls
        ]
        results: list = await asyncio.gather(*tasks)
        print(*results)


if __name__ == '__main__':
    asyncio.run(main())
