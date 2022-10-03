# 2) Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# [''ffff'.'3rfhg','4'] -> YES

mass = ['ffff','3rfhg','4']
result = 'No'
for i in mass:
    try:         # проверка 
        int(i)
        result = 'Yes'
        break
    except:
        pass
print(result)