def benchmark(func):
    """Декоратор, показывает время работы функции."""
    from datetime import datetime
    def wrapper(*args, **kwargs):
        start = datetime.now()
        res = func(*args, **kwargs)
        print(func.__name__, datetime.now() - start)
        return res
    return wrapper
