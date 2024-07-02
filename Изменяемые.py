a = set(map(int,input("Введите первый список чисел через пробел:").split()))
b = set(map(int,input("Введите второй список чисел через пробел:").split()))
difference = a.symmetric_difference(b)
print(list(difference))