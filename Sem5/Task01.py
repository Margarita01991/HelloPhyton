# В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, 
# чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
# Пример:
# Ввод: 1 2 4 5 -> 3

lst = [1, 2, 3, 4, 6, 7]
for i in range(1, len(lst)):
    if lst[i]-1 != lst[i-1]:
        print(lst[i-1]+1)