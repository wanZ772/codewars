def summation(num):
    total_sum = 0
    for i in range(num+1):
        total_sum += i
    return total_sum

print(summation(8))