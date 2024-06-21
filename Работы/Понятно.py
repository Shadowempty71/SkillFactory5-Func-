def multiplic_func(m):
    nonlocal_m = m
    def question_func(n):
        return n*nonlocal_m
    return question_func
two_mul = multiplic_func(2#m)
#на самом деле, two_mul присваивается функция question_func)
print(two_mul(5))