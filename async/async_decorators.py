import time
from functools import wraps


def async_timer(func):
    """Таймер для корутин."""
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start: float = time.perf_counter()
        try:
            return await func(*args, **kwargs)
        finally:
            total: float = time.perf_counter() - start
            print(
                'Затраченное время на выполнение [{}] составило: {:.4f}'.format(
                    func.__name__.upper(), total
                )
            )
    return wrapper
