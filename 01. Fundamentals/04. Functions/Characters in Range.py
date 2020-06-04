def in_between(start, end):
    char_li = []
    if ord(start) > ord(end):
        switch = end
        end = start
        start = switch
    for char in range(ord(start)+1, ord(end)):
        char_li.append(chr(char))
    result = " ".join(char_li)
    return result


born = input()
dead = input()

print(in_between(born, dead))