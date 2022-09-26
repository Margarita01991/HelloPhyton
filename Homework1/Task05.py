# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

xa,ya = float(input('Введите X:')),float(input('Введите Y:'))
pointA = [xa, ya]
xb,yb = float(input('Введите X:')),float(input('Введите Y:'))
pointB = [xb, yb]
distance = ((pointB[0] - pointA[0]) ** 2 + (pointB[1] - pointA[1]) ** 2) ** (0.5)
C = round(distance, 2)
print(f"Расстояние между точками A и B: {C}")