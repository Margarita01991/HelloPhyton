# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов. 
# 2*x² + 4*x + 5 
# 3*x² +10*x + 6 
# Вывод: 5*x² + 14*x + 11
import sympy 

with open('polinom_1.txt', 'w') as file:
    file.write('2*x**2 + 4*x + 5')
with open('polinom_2.txt', 'w') as file:
    file.write('3*x**2 + 10*x + 6')

with open('polinom_1.txt','r') as file:
    a = file.readline()
    # list1 = polinom_1.split()

with open('polinom_2.txt','r') as file:
    b = file.readline()
    # list2 = polinom_2.split()

print(f'{a} + {b}')
sum_polinom = sympy.simplify(a+'+'+b)
print(str(sum_polinom))

with open('sum_polinom.txt', 'w') as file:
    file.write(str(sum_polinom))
