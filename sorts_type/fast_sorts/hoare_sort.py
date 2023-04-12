import random


def hoare_sort(alist: list) -> None:
    """
    Сортировка Тони Хоара или быстрая сортировка.
    ---
    Сортировка работает in-place, то есть изменяет
    исходный списк, а не возвращает новый.
    ---
    Недостатки данной реализации:
        - необходима дополнительная память O(N).
    """
    if len(alist) <= 1:
        return

    pivot: int = random.choice(alist)

    left: list = []
    middle: list = []
    right: list = []

    for elem in alist:
        if elem < pivot:
            left.append(elem)
        elif elem == pivot:
            middle.append(elem)
        else:
            right.append(elem)

    hoare_sort(left)
    hoare_sort(right)

    alist[:] = left + middle + right


if __name__ == '__main__':

    def test_cases(data: tuple) -> None:
        for alist, sorted_list in data:
            hoare_sort(alist)
            assert alist == sorted_list

    a: list = random.sample(range(1, 10), 9)
    lsort: list = sorted(a)

    data: tuple = (
        (a, lsort),
    )

    test_cases(data)
