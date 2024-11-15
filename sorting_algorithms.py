import random as rn
import time
import timeit
from math import factorial


random = rn.SystemRandom()
arr = [5, 22222, 54, 8, 6, 9, 67, 124, 874, 12458, 657, 9898, 234, 5678, 97, 23345, 767, 2342, 123, 54684, 87664,
       21, 576, 9898, 5675, 769, 567, 97895675, 67967967856, 5675685, 780979, 35634, 345345]


def bubble_sort(arr: list) -> list:
    arr_len = len(arr)

    if arr_len <= 1:
        return arr

    for i in range(arr_len):
        # Флаг для оптимизации: если за проход не было обменов, массив отсортирован
        swapped = False
        for j in range(arr_len - 1 - i):  # Уменьшаем диапазон, так как последние элементы уже отсортированы
            first = arr[j]
            second = arr[j + 1]
            if first > second:
                arr[j] = second
                arr[j + 1] = first
                swapped = True
        # Если не было обменов, выходим из цикла
        if not swapped:
            break

    return arr


def is_sorted(arr: list) -> bool:
    if arr:
        arr_copy = arr.copy()
        arr_copy.sort()

        return arr_copy == arr

    return False


def bogo_sort(arr: list) -> list:
    ans_arr = []
    arr_copy = arr.copy()

    if len(arr) <= 1:
        return arr

    while True:
        if is_sorted(ans_arr):
            break

        random.shuffle(arr_copy)
        ans_arr = arr_copy

    return ans_arr


if __name__ == '__main__':
    print(f"""\tBogo sort O({len(arr)}!) or O({factorial(len(arr))}),
    approximately in seconds: 69466541000000000000000000000000""")
    start = time.time()
    print(bogo_sort(arr))
    end = time.time()
    print(f"Time: {end-start}")
