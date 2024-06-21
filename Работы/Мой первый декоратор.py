import time

def time_to_fib(func):
    def wrapper():
        time1 = time.time()
        print(f'Функция была запущена в {time1}')
        result = func()
        time2 = time.time()
        r = time1 - time2
        print(f'Функция была закончена в {time2}')
        print(f'Время затраченное на выполнение функции {r}')
        return result
    return wrapper

@time_to_fib
def fib():
    a,b = 0,1
    yield a
    yield b
    while b < 100000:
        a,b = b, a+b
        yield b

# decorator = time_to_fib(fib)
# decorator()
fib()
