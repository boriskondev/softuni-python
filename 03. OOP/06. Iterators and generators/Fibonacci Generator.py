def fibonacci():
    a = 0
    b = 1
    yield a
    yield b
    while True:
        c = a + b
        yield c
        a = b
        b = c


generator = fibonacci()

for i in range(5):
    print(next(generator))

