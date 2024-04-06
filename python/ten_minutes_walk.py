def is_valid_walk(walk):
    if len(walk) == 10:
        x,y = 0,0
        direction = {'n':1,'s':-1,'e':1,'w':-1}
        for i in walk:
            if i in 'ns':
                x += direction[i]
            else:
                y += direction[i]
        if x == 0 and y == 0:
            return True
    return False

print(is_valid_walk(['s', 'e', 'w', 'n', 's', 's', 'e', 'w', 'n', 's']))