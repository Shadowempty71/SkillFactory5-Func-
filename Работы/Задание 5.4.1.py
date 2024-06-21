# Создать функцию-генератор, возвращающую бесконечную последовательность
# натуральных чисел. По умолчанию она начинается с единицы, её шаг равен 1,
# но пользователь может указать любой шаг и любое число в качестве аргумента функции,
# с которого будет начинаться последовательность.

# Моё
def infinity(start = 1, step = 1):
    count = start
    yield count
    while count < 10:
        count += step
        yield count
for i in infinity():
    print (i)

#  Ещё можно так:
# inf - infinity(100, 10)
# for i in range(10):
#     print(next(inf))


# С сайта
# def count(start=1, step=1):
#     counter = start
#     while True:
#         yield counter
#         counter += step
