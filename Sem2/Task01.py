# Словарь
# a = {1:3,4:2,'Olga':18}
# b = {'Кошка':'Cat'}
# a.update({2:6})
# print(a)

# Генерация списка
# a = [i**2 for i in range(10)] # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# b = [i**2 for i in range(10)] # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81] квадраты чисел от 0 до 9
# c = {i:i**2 for i in range(10)}  # словарь квадратов чисел с ключевым значением {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
# cor = int(input()) 
# print(a,b,c)
# print(c[cor])
# Принимает на вход число и выдает последовательность из N членов
N = int(input('Введите число N: '))
P = [-i * -3 for i in range(N)]
print(P)
# Каждый следующий член прогрессии получаем умножением предыдущего на 3n+1
number = int(input('Введите число: '))
print(number)
n = [number*3 + 1 for number in range(8)]
print(n)