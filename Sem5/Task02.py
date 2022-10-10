# Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. 
# Порядок элементов менять нельзя.
# Пример:
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
num = [11, 5, 2, 3, 4, 6, 1, 7, 9, 8, 10]
def nextmax(lst):    
    max = lst[0]
    res = [lst[0]]
    for i in range(len(lst)):
        if lst[i] > max:
            max = lst[i]
            res.append(max)
    if len(res) == 1:
        nextmax(lst[1:])
    return res
print(nextmax(num))