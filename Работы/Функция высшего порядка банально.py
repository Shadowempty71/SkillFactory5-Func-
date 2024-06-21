def funcX2(func):
   return func(), func()

def func():
    print('Hello')

ppr = funcX2(func)

ppr()