def order(msg):
    # msg = msg.split(" ")
    arrangement = []
    sorted_msg = []
    for i in msg.split(" "):
        for j in range(1,10):
            if str(j) in i:
                arrangement.append(j-1)
    for k in arrangement:
        sorted_msg.append(msg.split()[k])
    print(arrangement)
    return " ".join(sorted_msg)
print(order("g3ood 4of the2 pe6ople th5e Fo1r' should equal 'Fo1r the2 g3ood 4of th5e pe6ople"))