# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
def multNumb(n):
    lst =[]
    for i in range(1, n + 1):
        if i == 1:
            lst.append(i) 
        else:
            lst.append(lst[i - 2] * i) 
    return lst
n = int(input('Введите число: '))
print(n)
print(multNumb(n))
