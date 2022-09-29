# 4. Задайте список из 2N+1 элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры.

N = int(input('Enter number: ')) 
from random import randint
numbers = []
M = 2*N+1
for i in range(M):
    numbers.append(randint (-N,N))
print(numbers)
def list(numbers):
    count =0 
    for element in numbers:
        count +=1
    return count
print('len: ', list(numbers))
first = int(input('Введите номер первого элемента: '))
second = int(input('Введите номер второго элемента: '))
if first > (len(numbers)) or second > (len(numbers)):
    print('Указанный элемент вне списка')
else:
    for i in range(len(numbers)):
        product = numbers[first -1]*numbers[second - 1]
    print(f'Произведение: {numbers[first -1]} * {numbers[second -1]} =', product)
