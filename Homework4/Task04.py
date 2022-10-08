# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0 (for 2,1, 0 степень)

import random
def write_file(str):
    with open('file1.txt', 'w') as data:
        data.write(str)
def rnd():
    return random.randint(0,101)
def create_polynomial(k):
    lst = [rnd() for i in range(k+1)]
    return lst
def create_str(sp):
    lst = sp[::-1]
    polinom = ''
    if len(lst) != 0:
        for i in range(len(lst)):
            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
                polinom += f'{lst[i]}x^{len(lst)-i-1}'
                if lst[i+1] != 0:
                    polinom += ' + '
            elif i == len(lst) - 2 and lst[i] != 0:
                polinom += f'{lst[i]}x'
                if lst[i+1] != 0:
                    polinom += ' + '
            elif i == len(lst) - 1 and lst[i] != 0:
                polinom += f'{lst[i]} = 0'
            elif i == len(lst) - 1 and lst[i] == 0:
                polinom += ' = 0'
    else:
        polinom = 'x = 0'
    return polinom
k = int(input("Введите  степень k = "))
koef = create_polynomial(k)
write_file(create_str(koef))
path = 'file1.txt'
data = open ('file1.txt', 'r')
for line in data:
    print(line)
data.close