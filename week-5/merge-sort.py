# Step 1 - Divide and conquer
# Step 2 - Intercalates
def merge_sort(v, start, end):
    if start < end:
        middle = (start + end) // 2
        merge_sort(v, start, middle)
        merge_sort(v, middle + 1, end)
        intercalates(v, start, middle, end)
    return v


def intercalates(v, start, middle, end):
    # Auxiliary arrays
    l = v[start: middle + 1] # Excludes middle
    r = v[middle + 1:end + 1] # Includes middle and ending values

    # Sentinel values, may change
    l.append(999)
    r.append(999)

    print('left:', l)
    print('right:', r)

    # Pointers
    i = 0
    j = 0

    for k in range(start, end + 1): # Need to include the latest item
        # If left side is lower than right side, than get the left side
        if l[i] <= r[j]:
            v[k] = l[i]
            i += 1
        # Otherwise the right side is the lower one
        else:
            v[k] = r[j]
            j += 1


unordered_list = [5, 2, 4, 7, 1, 3, 2, 6]
print(merge_sort(unordered_list, 0, len(unordered_list) - 1))
