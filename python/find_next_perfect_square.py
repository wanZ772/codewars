from math import sqrt

def find_next_square(sq):
    if sq > 0 and sq % sqrt(sq) == 0:
        sq += 1
        while sq % sqrt(sq) != 0:
            sq += 1
        return sq
    
    return -1

print(find_next_square(0))