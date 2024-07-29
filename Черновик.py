# Пробую реализацию поочерёдного хода крестика и нолика
field =[['-'] * 3 for i in range(3)]

def demonstration():# функция вывода игрового поля в консоль в консоль
    print(f"  0 1 2")
    print(f"0 {field[0][0]} {field[0][1]} {field[0][2]}")
    print(f"1 {field[1][0]} {field[1][1]} {field[1][2]}")
    print(f"2 {field[2][0]} {field[2][1]} {field[2][2]}")

def move(): # функция ввода координат и проверки возможности хода
    while True:
        x_y = input("Ваш ход. Введите числа через пробел:").split()
        if len(x_y) != 2:
            print("Вы ввели не верные координаты. Попробуйте ввести числа через пробел")
            continue
        else:
            x,y = x_y
            x,y = int(x),int(y)
        if any((2 < item) or (item < 0) for item in(x, y)):
            print("Ход недопустим, - выбранная клетка вне игрового поля.Попробуйте сходить иначе")
            continue
        elif field[x][y] != '-':
            print("Ход недопустим, - выбранная клетка занята.Попробуйте сходить иначе")
            continue
        else:
            return x,y

num = 0 # поочерёдные ходы
print("Первым ходит крестик")
while num < 9:
    num += 1

    demonstration()
    x, y = move()
    if num %2 == 1:
        print("Сейчас ходит нолик")
        field[x][y] = "X"
    else:
        print("Сейчас ходит крестик")
        field[x][y] = "0"

