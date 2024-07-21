field =[['-'] * 3 for i in range(3)] # игровое поле
field[2][2] = 'X'

def move():
    while True:
        x,y = map(int, input("Ваш ход. Введите числа через пробел:").split())
        x,y = [x,y]
        print(len(xy))
        print(type(x_y))
        print(x_y)
        if len(x_y) != 2:
            print("Вы ввели не правильные координаты. Попробуйте ввести числа через пробел")
            continue
        else:
            x,y = x_y[0], x_y[1]
    while True:
        if any((2 < item) or (item < 0) for item in(x, y)):
            print("Ход недопустим, - выбранная клетка вне игрового поля.Попробуйте сходить иначе")
            x, y = map(int, input("Введите числа через пробел:").split())
        elif field[x][y] != '-':
            print("Ход недопустим, - выбранная клетка занята.Попробуйте сходить иначе")
            x, y = map(int, input("Введите числа через пробел:").split())
        else:
            return x, y

move()