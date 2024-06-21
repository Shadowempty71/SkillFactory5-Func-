a = 18
print(id(a))
def gtry():
    global a
    print("Число вызванное из глобальной области", a)
    print(id(a))
    a = 20
    print(id(a))
    b = 15
    return a
print(gtry())
print(a)
print(id(a))

