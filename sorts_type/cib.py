"""
Набор квадратичных сортировок.
Каждая из сортировок имеет асимптотику: O(N * N)
"""

def choice_sort(alist: list) -> list:
    """Сортировка методом выбора."""
    for i in range(len(alist) - 1):
        for j in range(i + 1, len(alist)):
            if alist[j] < alist[i]:
                tmp = alist[i]
                alist[i] = alist[j]
                alist[j] = tmp
    return alist


def insert_sort(alist: list) -> list:
    """Сортировка вставкой."""
    for i in range(1, len(alist)):
        temp = alist[i]
        j: int = i - 1
        while j >= 0 and temp < alist[j]:
            alist[j + 1] = alist[j]
            j -= 1
        alist[j + 1] = temp
    return alist


def bubble_sort(alist: list) -> list:
    """Сортировка методом пузырька."""
    n: int = len(alist)
    swap: bool = False
    while n > 0:
        for i in range(n - 1):
            if alist[i] > alist[i + 1]:
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp
                swap = True
        n -= 1
        if not swap:
            break
    return alist


if __name__ == '__main__':
    import random

    def test_cases(data: dict) -> None:
        for sorting_func, (args, expected) in data.items():
            assert sorting_func(args) == expected, sorting_func


    a: list = random.sample(range(1, 10), 9)
    lsort: list = sorted(a)

    data: dict = {
        choice_sort: (list(a), lsort),
        insert_sort: (list(a), lsort),
        bubble_sort: (list(a), lsort),
    }

    test_cases(data)
