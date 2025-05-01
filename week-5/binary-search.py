import random


def binary_search(v, search, start, end):
    sorted_list = sorted(v)

    middle = (start + end) // 2

    if end < start:
        return -1

    if search == sorted_list[middle]:
        return middle

    if search < sorted_list[middle]:
        return binary_search(sorted_list, search, start, middle - 1)

    if search > sorted_list[middle]:
        return binary_search(sorted_list, search, middle + 1, end)

    return None


unordered_list = random.sample(range(100), 20)
print(binary_search(unordered_list, 29, 0, len(unordered_list)))
