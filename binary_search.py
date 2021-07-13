import random


def binary_search(arr, start, end, obj):
    print(f'Looking for {obj} between {arr[start]} and {arr[end - 1]}')

    if start >= end:
        return False

    middle = (start + end) // 2

    if arr[middle] == obj:
        return True

    elif obj < arr[middle]:
        return binary_search(arr, start, middle, obj)
    elif obj > arr[middle]:
        return binary_search(arr, middle + 1, end, obj)


if __name__ == '__main__':
    arr_size = int(input('List size: '))
    objective = int(input('Number to find: '))

    arr = sorted([random.randint(0, 100) for i in range(arr_size)])
    # print(arr)
    found = binary_search(arr, 0, len(arr), objective)
    print(arr)
    print(f'The element {objective} {"is" if found else "is not"} on the list')
