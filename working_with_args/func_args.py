def func_with_args(*args) -> tuple:
    return args


def func_with_kwargs(**kwargs) -> dict:
    return kwargs


def func_with_args_and_kwargs(*args, **kwargs) -> list:
    return [args, kwargs]


def tests() -> None:
    assert func_with_args('Simbos', 6) == ('Simbos', 6)
    assert isinstance(func_with_args(), tuple) == True
    assert func_with_kwargs(name='Simbos', age=6) == {'name': 'Simbos', 'age': 6}
    assert isinstance(func_with_kwargs(), dict) == True
    assert func_with_args_and_kwargs('Simbos', age=6) == [('Simbos',), {'age': 6}]


if __name__ == '__main__':
    tests()
