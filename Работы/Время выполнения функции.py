import time
def decorator_time(func):
    def wrapper():
        print(f"Запустилась функция {func}")
        t0 = time.time()
        result = func()
        dt = time.time() - t0
        print(f"Функция выполнилась. Время : {dt:.10f}")
        return dt
    return wrapper()

def pow_2():
    return 1000000**2

def in_duild_pow():
    return pow(1000000, 2)

pow_2 = decorator_time(pow_2)
in_duild_pow = decorator_time(in_duild_pow)

pow_2()

in_duild_pow()