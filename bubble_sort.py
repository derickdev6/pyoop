import random


def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


if __name__ == '__main__':
    arr_size = int(input('List size: '))

    arr = [random.randint(0, 50) for i in range(arr_size)]
    print(arr)
    print(bubble_sort(arr[::]))
