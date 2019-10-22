x = 5
y = 9


def state(tup):
    x = tup[0]
    y = tup[1]
    return x * y


move = (x, y)

print(state(move))