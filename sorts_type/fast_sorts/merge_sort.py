def merge(left: list, right: list) -> list:
    """
    Слияние отсортированных списков.
    ---
    Аргументы:
        - два отсортированных списка.
    ---
    Возвращаемое значение:
        - цельный список.
    """
    buffer: list = []
    i: int = 0
    j: int = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            buffer.append(left[i])
            i += 1
        else:
            buffer.append(right[j])
            j += 1

    while i < len(left):
        buffer.append(left[i])
        i += 1

    while j < len(right):
        buffer.append(right[j])
        j += 1

    return buffer


def merge_sort(alist: list) -> None:
    """
    Рекурентная сортировка слиянием.
    ---
    Аргументы:
        - список, который необходимо отсортировать.
    ---
    Возвращаемое значение:
        - None, т.к. сортировка происходит in-place.
    """
    if len(alist) <= 1:
        return

    middle: int = len(alist) // 2
    left: list = alist[:middle]
    rigth: list = alist[middle:]

    merge_sort(left)
    merge_sort(rigth)

    alist[:] = merge(left, rigth)


if __name__ == '__main__':
    import random

    def test_cases(data: tuple) -> None:
        for alist, sorted_list in data:
            merge_sort(alist)
            assert alist == sorted_list

    a: list = random.sample(range(1, 10), 9)
    lsort: list = sorted(a)

    data: tuple = (
        (a, lsort),
    )

    test_cases(data)
