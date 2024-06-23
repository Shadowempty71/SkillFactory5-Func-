a = set(map(int,input("Введите числа первой последовательности:").split()))
b = set(map(int,input("Введите числа второй последовательности:").split()))
с = a.symmetric_difference(b)
print(с)