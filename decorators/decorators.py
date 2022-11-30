def is_odd_or_even(numbers):
    """Декоратор для проверки списка на четность чисел."""
    def wrapper(*args):
        result: list[tuple[int, bool]] = []
        for number in numbers(*args):
            result.append(
                (
                    number,
                    'Odd' if bool(number % 2) else 'Even'
                )
            )
        return result
    return wrapper


@is_odd_or_even
def get_list(numbers: list[int]) -> list[int]:
    return numbers


# Тесты для декоратора
list_of_numbers: list[int] = [int(x) for x in range(0, 3)]

assert get_list(list_of_numbers) == [(0, 'Even'), (1, 'Odd'), (2, 'Even')]
assert get_list([2, 2, 2]) == [(2, 'Even'), (2, 'Even'), (2, 'Even')]
assert get_list([-1]) == [(-1, 'Odd')]
assert get_list([0]) != [(0, 'Odd')]