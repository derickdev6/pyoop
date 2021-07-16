import random


def backpack(capacity, weights, values, n):

    # If finished elements or if capacity is full return 0
    if n == 0 or capacity == 0:
        return 0

    # If next element doesn't fit the backpack skip it
    if capacity - weights[n - 1] < 0:
        return backpack(capacity, weights, values, n - 1)

    # Decides wether its better to pick an item or not, recursively
    return max(values[n - 1] + backpack(capacity - weights[n - 1], weights, values, n - 1),
               backpack(capacity, weights, values, n - 1))


if __name__ == '__main__':
    # Ask for item qnty
    items = int(input('Items: '))

    # Create items randomly
    values = [random.randint(10, 30) for i in range(items)]
    weights = [random.randint(15, 25) for i in range(items)]
    print(f'Values = \t{values}\nWeights = \t{weights}')

    # Asks for capacity
    capacity = int(input('Capacity: '))

    # Uses solution
    result = backpack(capacity, weights, values, items)
    print(result)
