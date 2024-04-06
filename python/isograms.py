def is_isogram(string):
    duplicates = []
    for i in string.lower():
        if i in duplicates:
            return False
        duplicates.append(i)
    return True
print(is_isogram("moose"))