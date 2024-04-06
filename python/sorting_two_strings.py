def longest(a1, a2):
    duplicates = ""
    for i in a1+a2:
        if i not in duplicates:
            duplicates += i
    return ''.join(sorted(duplicates))

    ## one line code
    return ''.join(sorted(set(a1+a2)))

print(longest("aretheyhere", "yestheyarehere"))