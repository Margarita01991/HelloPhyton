# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint
lst1 = [randint(-10, 10) for i in range(10)]
lst2 = []
amount = 0
print (lst1)
for i in range(len(lst1)):
    if i%2 != 0:
        lst2.append(lst1[i])
        amount += lst1[i]
print(lst2)
print(amount)
