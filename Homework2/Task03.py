# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
# *Пример:*
# - Для n = 6: [2.0, 2.25, 2.37037037037037, 2.44140625, 2.4883199999999994, 2.5216263717421135]

n = int(input('Enter number: ')) 
def list(n):
    return[round((1 + 1 / number)**number, 16) for number in range (1, n + 1)]       
print(list(n))
print(round(sum(list(n)), 2))