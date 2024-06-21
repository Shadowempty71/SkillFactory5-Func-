def fib():
    a, b = 1, 2
    yield a
    yield b
    while True:
        a,b  = b, a+b
        yield b

for i in fib():
    print(i)