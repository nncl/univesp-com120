# Divide and conquer algorithm
# Split vectors into smaller ones
# Uses a pivot, which generally we choose the element in the middle

def quick_sort(array, start, end):
    middle = (start + end) // 2
    pivot = array[middle]

    # Pointers
    i = start
    j = end

    while i < j:  # Until pointer crosses each other
        # Goes from the left to the right (until it finds an element greater than or equal to the pivot)
        # ->
        while array[i] < pivot:
            i += 1

        # Same from the right to the left ('til find an element less than or equal to the pivot)
        # <-
        while array[j] > pivot:
            j -= 1

        # Swap elements if pointers haven't crossed, then move inward
        # TD: Shouldn't we compare the items instead of the indexes? No, this statement is for checking if the pointers have
        #    crossed each other
        # TD: How does it already know it can switch? Because of the whiles above: when they're no long true,
        #   we know elements are in the wrong side.
        #   Quick sort relies on when that’s no longer true — that's when the value needs to be moved to the other side
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    # Check the subsets
    if j > start:
        quick_sort(array, start, j)
    if i < end:
        quick_sort(array, i, end)


unordered_list = [25, 57, 35, 37, 12, 86, 92, 33]
quick_sort(unordered_list, 0, len(unordered_list) - 1)
print(unordered_list)
