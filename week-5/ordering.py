# Step 1 - Compares each element with its successor
# Step 2 - Compares each ordered element until before the last ordered element,
#   due to the latest one is now already ordered
def bubble_sort(v):
    for i in range(len(v) - 1): # Step 1
        for j in range(len(v)-i-1): # Step 2: excluding latest element
            if v[j] > v[j + 1]:
                v[j], v[j + 1] = v[j + 1], v[j]

    return v

unordered_list = [4,5,4,3,3,7,5,99,8,72,599,0,1]
print(bubble_sort(unordered_list))