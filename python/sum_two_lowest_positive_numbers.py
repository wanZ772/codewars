def sum_two_smallest_numbers(numbers):
    # with python sorted function
    # sort = sorted(numbers)
    # return sort[0] + sort[1]

    #without python sorted function
    swap = True
    while swap:
        swap = False
        for i in range(len(numbers) - 1):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[ i + 1], numbers[i]
                swap = True
    return numbers[0] + numbers[1]

        

print(sum_two_smallest_numbers([19, 5, 42, 2, 77]))