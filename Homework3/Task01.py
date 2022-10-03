# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint
list1 = [randint(-10, 10) for i in range(10)]
list2 = []
sum = 0
print (list1)
for i in range(len(list1)):
    if i%2 != 0:
        list2.append(list1[i])
        sum += list1[i]
print(list2)
print(sum)
