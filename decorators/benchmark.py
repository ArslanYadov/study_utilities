def benchmark(func):
    """Декоратор, показывает время работы функции."""
    import logging
    from datetime import datetime
    def wrapper(*args, **kwargs):
        start = datetime.now()
        res = func(*args, **kwargs)
        logging.info(
            f'Function name: \"{func.__name__}\"; '
            f'Time: {datetime.now() - start}.'
        )
        return res
    return wrapper


@benchmark
def list_with_big_values():
    return [int(x**x) for x in range(10000, 20000)]


if __name__ == '__main__':
    import logging
    logging.basicConfig(
        level=logging.INFO,
        format='[%(levelname)s] : %(message)s'
    )
    list_with_big_values()
