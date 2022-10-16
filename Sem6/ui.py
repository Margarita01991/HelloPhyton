import model
from logger import log_expr


def get_expr(): # метод получения информации
    return input()

def show_res(a): # вызов результата в консоль, принимая результат из model.py
    print(a)
# a=get_expr()


expression = get_expr() # получение уравнения от пользователя
log_expr(expression) # логирует информацию, которая лежит в expression
answer = model.evaluate_expr(expression) # сохранение решения

show_res(answer) # вывод ответа