from datetime import datetime
from functools import wraps


def logit(file='main.log', _time=datetime.now()):
    def logging_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            log_str: str = '<{}> исполнена в [{}]'.format(
                func.__name__, _time
            )
            with open(file, 'a') as fout:
                fout.write(log_str + '\n')
                fout.truncate()
        return wrapper
    return logging_decorator
