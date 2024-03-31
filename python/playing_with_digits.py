def dig_pow(n,p):
    num = []
    output = 0
    for i in str(n):
        num.append(i)
    for i in range(len(num)):
        output += (int(num[i]) ** (p + i))    
    print(output)
    return int(output / n) if (output % n == 0) else -1
print(dig_pow(46288, 5))