# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random
list1 = [random.randint(0,15) for i in range (20)]
print(list1)
list2 =[]
[list2.append(i) for i in list1 if i not in list2]
print(list2)
