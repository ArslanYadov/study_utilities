def merge(alist: list, blist: list) -> list:
    """
    Слияние отсортированных списков.
    ---
    Аргументы:
        - два отсортированных списка.
    ---
    Возвращаемое значение:
        - цельный список.
    """
    merge_list: list = [0] * (len(alist) + len(blist))
    i: int = 0
    j: int = 0
    k: int = 0

    while i < len(alist) and j < len(blist):
        if alist[i] <= blist[j]:
            merge_list[k] = alist[i]
            i += 1
        else:
            merge_list[k] = blist[j]
            j += 1
        k += 1

    while i < len(alist):
        merge_list[k] = alist[i]
        i += 1
        k += 1

    while j < len(blist):
        merge_list[k] = blist[j]
        j += 1
        k += 1

    return merge_list


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
