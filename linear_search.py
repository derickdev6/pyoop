import random


def linear_search(arr, obj):
    match = False

    for element in arr:
        if element == obj:
            match = True
            break

    return match


if __name__ == '__main__':
    arr_size = int(input('List size: '))
    objective = int(input('Number to find: '))

    arr = [random.randint(0, 1000000) for i in range(arr_size)]
    # print(arr)
    found = linear_search(arr, objective)

    print(f'The element {objective} {"is" if found else "is not"} on the list')
