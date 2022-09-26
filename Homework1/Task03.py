# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).
# Пример:
#  x=34; y=-30 -> 4
#  x=2; y=4-> 1
#  x=-34; y=-30 -> 3

x,y = int(input('Введите X:')),int(input('Введите Y:'))
list = [x, y]
if(list[0] > 0 and list[1] > 0):
    print("list in 1 quart")
elif(list[0] < 0 and list[1] > 0):
    print("list in 2 quart")
elif(list[0] < 0 and list[1] < 0):
    print("list in 3 quart")
elif(list[0] > 0 and list[1] < 0):
    print("list in 4 quart")
else: 
    print("точка лежит на оси")
