def count_sort(alist: list, k: int) -> list:
    """
    Сортировка подсчетом.
    ---
    Аргументы:
        - список и самое большое значение в этом списке.
    ---
    Возвращаемое значение:
        - отсортированный в неубывающем порядке список.
    ---
    Скорость выполнения: O(N);
    Затраты по памяти: O(M), где М - количество элементов (k + 1).
    """
    counter: list = [0] * (k + 1)
    for i in range(len(alist)):
        counter[alist[i]] += 1

    counter[0] -= 1
    for i in range(1, k + 1):
        counter[i] = counter[i] + counter[i - 1]

    asort: list = [None] * len(alist)
    for elem in alist[::-1]:
        asort[counter[elem]] = elem
        counter[elem] -= 1

    return asort


if __name__ == '__main__':

    def test_cases(data: dict) -> None:
        for args, expected in data.items():
            assert count_sort(*args) == expected

    alist: tuple = (6, 4, 5, 3)
    k: int = max(alist)
    asort: list = sorted(alist)

    data: dict = {
        (alist, k): asort,
    }

    test_cases(data)
