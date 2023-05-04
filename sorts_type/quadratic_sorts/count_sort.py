def count_sort(alist: list) -> list:
    """
    Сортировка подсчетом.
    ---
    Аргументы:
        - список.
    ---
    Возвращаемое значение:
        - отсортированный в неубывающем порядке список.
    ---
    Асимптотика: O(N + M);
    Затраты по памяти: O(N + M).
    """
    k: int = max(alist) + 1
    counter: list = [0] * k
    for i in range(len(alist)):
        counter[alist[i]] += 1

    counter[0] -= 1
    for i in range(1, k):
        counter[i] = counter[i] + counter[i - 1]

    asort: list = [None] * len(alist)
    for elem in alist[::-1]:
        asort[counter[elem]] = elem
        counter[elem] -= 1

    return asort


def count_sort_in_place(alist: list) -> None:
    """Сортировка подсчетом на месте.
    ---
    Аргументы:
        - список.
    ---
    Возвращаемое значение:
        - отсутствует (None), т.к. сортировка на месте.
    ---
    Асимптотика: O(N^2);
    Затраты по памяти: O(N).
    """
    counter: list = [0] * (max(alist) + 1)
    for i in range(len(alist)):
        counter[alist[i]] += 1

    i: int = 0
    for j in range(len(counter)):
        for _ in range(counter[j]):
            alist[i] = j
            i += 1


if __name__ == '__main__':

    def test_(cases: dict) -> None:
        for case in cases:
            if case == 'extra':
                args: list = cases[case]
                expected: list = sorted(args)
                assert count_sort(args) == expected
            else:
                args: list = list(cases[case])
                expected: list = sorted(args)
                count_sort_in_place(args)
                assert args == expected

    alist_0: tuple = (6, 4, 5, 3)
    alist_1: tuple = (1, 5, 2, 3, 2, 2, 5, 2, 3, 1, 3, 0, 3, 2, 5, 5)

    cases: dict = {
        'extra': alist_0,
        'in-place': alist_1,
    }

    test_(cases)
