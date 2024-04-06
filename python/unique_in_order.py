def unique_in_order(sequence):
    elements = []
    for i in range(len(sequence) -1):
        if sequence[i] != sequence[i+1]:
            elements.append(sequence[i])
    return elements
print(unique_in_order('AAAABBBCCDAABBB'))