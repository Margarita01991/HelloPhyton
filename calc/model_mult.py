# метод, отвечающий за инициализацию начальных значений переменных x, y
x = 0
y = 0

def init(a, b):
    global x
    global y
    x=a
    y=b


# метод, возвращающий сумму переменных x, y

def do_it():
    return x * y