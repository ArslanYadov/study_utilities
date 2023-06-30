def grep_coroutine(pattern: str):
    """Мини греп в виде корутины."""
    print('Searching for', pattern, 'with coroutine...')

    while True:
        line = yield
        if pattern in line:
            yield line


def grep_decorator(pattern: str):
    """Мини греп в виде декоратора."""
    print('Searching for', pattern, 'with decorator...')

    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if pattern in result:
                return result
        return wrapper
    return decorator


def test_grep_coroutine(pattern: str, args: tuple, expected: str):
    """Тестим работу корутины."""
    search = grep_coroutine(pattern)
    next(search)
    for string in args:
        output = search.send(string)
        if output:
            print('Find pattern [%s] in "%s"' % (pattern, output))
            assert output == expected


def test_grep_decorator(pattern: str, args: tuple, expected: str):
    """Тестим работу декоратора."""
    @grep_decorator(pattern)
    def search(string: str):
        return string

    for string in args:
        output = search(string)
        if output:
            print('Find pattern [%s] in "%s"' % (pattern, output))
            assert output == expected


if __name__ == '__main__':
    strings: tuple = (
        'Eggs with extra ham for breakfast',
        'The answer to life, the universe and everything',
        'So many spam at my email account',
    )
    expected: str = strings[-1]
    pattern: str = 'spam'
    tests: tuple = (
        test_grep_coroutine,
        test_grep_decorator,
    )
    for test in tests:
        test(pattern, strings, expected)
