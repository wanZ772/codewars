def count_duplicate(text):
    check_duplicate = {}
    duplicate = []
    
    for i in text.lower():
        if i not in check_duplicate:
            check_duplicate[i] = 1
        else:
            check_duplicate[i] += 1
        
    for i in check_duplicate:
        if check_duplicate[i] > 1:
            duplicate.append(i)
    return len(duplicate)
print(count_duplicate("ABBA"))