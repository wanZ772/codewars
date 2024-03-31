def reverse_string(string):
    reverse = ''
    for i in string[::-1]:
        reverse += ''.join(i)
    return reverse
print(reverse_string("hello world"))