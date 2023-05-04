def radix_sort(arr: list) -> None:
    """
    Подразрядная сортировка. Реализация in-place.
    ---
    Асимптотика: O(N * M)
    """
    count_zero: list = []
    count_one: list = []

    period: int = len(bin(max(arr))[2:])
    for radix in range(period):
        for i in range(len(arr)):
            if arr[i] & (1 << radix) == 0:
                count_zero.append(arr[i])
            else:
                count_one.append(arr[i])
        arr[:] = count_zero + count_one
        count_zero = []
        count_one = []


if __name__ == '__main__':
    import random

    def test_(cases: tuple) -> None:
        for args in cases:
            expected = sorted(args)
            radix_sort(args)
            assert args == expected, args

    arr_0: list = [0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1]
    arr_1: list = [1, 5, 2, 3, 2, 2, 5, 2, 3, 1, 3, 0, 3, 2, 5, 5]
    arr_rand: list = random.sample(range(1, 10), 9)

    cases: tuple = (arr_0, arr_1, arr_rand)

    test_(cases)
