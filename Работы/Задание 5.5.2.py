# Напишите декоратор, который будет подсчитывать
# количество вызовов декорируемой функции.
# Для хранения переменной, содержащей количество вызовов,
# используйте nonlocal область декоратора.

def decor(func):
    count = 0
    def wraper(*args,**kwargs):
        nonlocal count
        func(*args,**kwargs)
        count +=1
        print(f"Функция {func} была вызвана {count} раз")
    return wraper
@decor
def say_word(word):
    print(word)
say_word("Сумятица")
print("--------")
say_word("Книксен")
print("--------")
say_word("Сколопендра")
print("--------")