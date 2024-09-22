num = int(input("Введите целое число:"))
list_of_num = []
while num != 0:
    list_of_num.append(num)
    num = int(input("Введите целое число:"))
list_of_num.sort()
for i in list_of_num:
    print(i)
print(list_of_num)