'''f(x) = 18x^3+5x^2 + 10x - 30
Определить корни
Найти интервалы, на которых функция возрастает
Найти интервалы, на которых функция убывает
Построить график
Вычислить вершину
Определить промежутки, на котором f > 0
Определить промежутки, на котором f < 0
Необязательно, для интереса:
f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30'''
''''''
import sympy
from sympy import *
from sympy.abc import x

def out_blue(text):
    print("\033[34m {}" .format(text))

def out_white(text):
    print("\033[37m {}" .format(text))

out_blue ('Определить корни')
x = sympy.Symbol('x')
f = 18*x**3+5*x**2 + 10*x - 30
root = sympy.solve(f,x)
out_white(root)

out_blue ('Найти интервалы, на которых функция возрастает')
out_white(sympy.solve(f > 0,x))

out_blue ('Найти интервалы, на которых функция убывает')
out_white(sympy.solve(f < 0,x))

out_blue ('Вычислить вершину')
diff = sympy.diff(f,x)
# print(diff)
out_white(sympy.solve(diff,x))

out_blue('Определить промежутки, на котором f > 0')
out_white(sympy.solve(diff > 0,x))

out_blue ('Определить промежутки, на котором f < 0')
out_white(sympy.solve(diff < 0,x))

# Построить график
sympy.plotting.plot(f)
# sympy.plotting.plot3d(f) - график в 3D
