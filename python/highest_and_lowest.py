def hight_and_lower(numbers):
    list_numbers = []
    for i in numbers.split(' '):
        list_numbers.append(int(i))
    return f"{max(list_numbers)} {min(list_numbers)}"
print(hight_and_lower("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))