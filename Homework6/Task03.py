# Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.

# def square_numb (x):
#     return x ** 2

square_numb = lambda x: x**2
a,b = int(input('Введите число a: ')),int(input('Введите число b: '))
if a == square_numb(b):
    print (f'Число {a} является квадратом {b}')
elif b == square_numb(a):
     print (f'Число {b} является квадратом {a}')
else:
     print ('Числа не является квадратом друг друга')

