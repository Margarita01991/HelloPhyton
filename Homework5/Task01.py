# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
import random

def input_candy(name):
    x = int(input(f"{name}, сколько конфет от 1 до 28 вы возьмете: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите количество от 1 до 28: "))
    return x

def p_print(name, n, count, balance):
    print(f"{name}, взял {n}, теперь у него {count}. Осталось на столе {balance} конфет.")

player1 = 'Игрок 1'
player2 = 'Игрок 2'
balance = 2021 # можно ввести любое количество конфет
print('Случайный выбор первого хода...')
play = random.randint(0,2)

if play:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

count1 = 0 
count2 = 0

while balance > 28:
    if play:
        n = input_candy(player1)
        count1 += n
        balance -= n
        play = False
        p_print(player1, n, count1, balance)
    else:
        n = input_candy(player2)
        count2 += n
        balance -= n
        play = True
        p_print(player2, n, count2, balance)

if play:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")

