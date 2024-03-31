def persistence(n):
    count = 1
    while True:
        num = []
        multiplyer = 1
        if len(str(n)) != 1:
            for i in str(n):
                num.append(i)
            for i in num:
                multiplyer = multiplyer * int(i)
            if len(str(multiplyer)) == 1:
                return count
            else:
                count +=1
                n = multiplyer

        else:
            return 0

print(persistence(39))