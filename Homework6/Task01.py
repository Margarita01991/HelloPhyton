# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

import random
lst =[random.randint(1, 10) for i in range(10)]
lst1 = [lst[i] for i in range(0, len(lst), 2)]
print(lst)
print(lst1)
print(f'Сумма элементов на нечетных позициях = {sum(lst1)}')
