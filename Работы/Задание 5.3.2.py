#Написать функцию,которая будет перемножать
# любое количество переданных ей аргументов.
def mult(*nums):
    m = 1
    for i in nums:
        m *= i
    return m
print(mult(2,3,15,6))
#На сайте тоже самое