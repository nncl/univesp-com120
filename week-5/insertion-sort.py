# Orders set by inserting elements into an already ordered subset
def insertion_sort(v):
    for i in range(1, len(v)): # Starts by the second element, cause it's gonna compare it with the previous one
        current = v[i]
        previous = i - 1

        while previous >= 0 and v[previous] > current:
            v[previous + 1] = v[previous]
            previous -= 1

        v[previous + 1] = current

    return v

unordered_list = [44 , 55 , 12 , 42 , 94 , 18 , -10, -2, -12, 6 , 67]
print(insertion_sort(unordered_list))