def find_smallest_int(arr):
    # with python build-in feature
    # return min(arr) 

    # without python build-in feature
    small = arr[0]
    for i in arr:
        small = i if i <= small else small
    return small
print(find_smallest_int([34, 15, 88, 2]))