# Задача 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# ¬ инверсия (not), ⋀ - конъюнкция (and), ⋁ - дизъюнкция (or)

print('Проверить истинность утверждений ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z')
x,y,z = int(input('Введите X:')),int(input('Введите Y:')),int(input('Введите Z:'))
if not(x or y or z) == (not x and not y and not z):
    print(True)
else:
    print(False)