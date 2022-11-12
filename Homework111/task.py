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

import sympy
from sympy import *
from sympy.abc import x
'''
print ('Определить корни')
x = sympy.Symbol('x')
root = sympy.solve(18*x**3+5*x**2 + 10*x - 30,x)
print(root)

print ('Найти интервалы, на которых функция возрастает')
print(sympy.solve(18*x**3+5*x**2 + 10*x - 30 > 0,x))

print ('Найти интервалы, на которых функция убывает')
print(sympy.solve(18*x**3+5*x**2 + 10*x - 30 < 0,x))

print ('Вычислить вершину')
f = 18*x**3+5*x**2 + 10*x - 30
diff =  sympy.diff(f,x)
print(diff)
print(sympy.solve(diff,x))

print('Определить промежутки, на котором f > 0')
print(sympy.solve(diff > 0,x))

print ('Определить промежутки, на котором f < 0')
print(sympy.solve(diff < 0,x))

# Построить график
sympy.plotting.plot3d(18*x**3+5*x**2 + 10*x - 30)
'''
# print ('Определить корни')
# x = sympy.Symbol('x')
# root = sympy.solve(-12*x**4*sin(cos(x))-18*x**3+5*x**2 + 10*x - 30,x)
# print(root)

# print ('Найти интервалы, на которых функция возрастает')
# print(sympy.solve(-12*x**4*sin(cos(x))-18*x**3+5*x**2 + 10*x - 30,x))

# print ('Найти интервалы, на которых функция убывает')
# print(sympy.solve(-12*x**4*sin(cos(x))-18*x**3+5*x**2 + 10*x - 30,x))

# print ('Вычислить вершину')
# f = -12*x**4*sin(cos(x))-18*x**3+5*x**2 + 10*x - 30,x
# diff =  sympy.diff(f,x)
# print(diff)
# print(sympy.solve(diff,x))

# print('Определить промежутки, на котором f > 0')
# print(sympy.solve(diff > 0,x))

# print ('Определить промежутки, на котором f < 0')
# print(sympy.solve(diff < 0,x))

# # Построить график
x = sympy.Symbol('x')
sympy.plotting.plot(-12*x**4*sin(cos(x))-18*x**3+5*x**2 + 10*x - 30,x)

