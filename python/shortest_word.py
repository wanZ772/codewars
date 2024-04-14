def find_short(s):
    short = len(s.split(' ')[0])
    for i in s.split(' '):
        if len(i) < short:
            short = len(i)
    return short
print(find_short("bitcoin take over the world maybe who knows perhaps"))