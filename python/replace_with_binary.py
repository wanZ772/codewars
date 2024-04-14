def fake_bin(x):
    binary = ""
    for i in x:
        if int(i) < 5:
            binary = "0"
        else:
            binary = "1"
    return binary

print(fake_bin('45385593107843568'))