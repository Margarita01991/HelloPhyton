# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

number = int(input('Введите число: '))
list =[]
for i in range(1,number+1):
    if(number%i==0):
      list.append(i)
print(list)