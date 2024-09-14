time = (15,25,35,45,55,65)
def time_code(*args):
    calc = sum(*args)
    hour = calc%(60*24)//60
    minit = calc%60
    print(f"Общее время {hour}:{minit}")
time_code(time)