# print('Hello world')
# a = 123
# b = 1.23
# value = None

# print(a)
# print(b)
# print(value)
# value = 1234
# print(value)
# print(type(a))
# print(type(b))
# print(type(value))
#print(type(value))
# s = 'qwerty'
# print(s)
# print(type(s))
# d = "'qwe\nrty"
# print(d)
# print(a,b,s,d) 
# print(a,'-', b,'-', s,'-', d)
# print('{} - {} - {}'.format(a , b , s, d))
# print(f'{a} - {b} - {s}'.format(a , b , s, d))

# f = False
# print(f)
# print(type(f))
# list = [1, 2, 3, 'raf', True]
# print(list)

# print('введите a')
# a = input()
# print('введите b')
# b = input()
# print(a, b)
# # print('{} {}' .format(a, b))
# # print(f'{a} {b}')
# print(a, '+', b, '=', a+b)

# print('введите a')
# a = int(input())
# print('введите b')
# b = int(input())
# print(a, b)
# # print('{} {}' .format(a, b))
# # print(f'{a} {b}')
# print(a, '+', b, '=', a+b)

# print('введите a')
# a = float(input())
# print('введите b')
# b = float(input())
# print(a, b)
# # print('{} {}' .format(a, b))
# # print(f'{a} {b}')
# print(a, '+', b, '=', a+b)

# a = 1.31231223
# b = 3
# c = round(a * b, 7)
# print(c)
# print(type(c))

# a = 3
# a = a + 5
# print(a)

# a = 1 < 4 and 5 > 2
# print(a)

# a = 1 != 2
# print(a)

# a = [1, 2]
# b = [1, 2]
# print(a == b)

# funk = 1
# T = 4
# x = 2
# print(funk<T>x)

# f = 1 > 2 or 4 < 6
# print(f)

# f = [1,2,3,4]
# print(f)
# print(2 in f) # содердит 2
# print(not 2 in f) # список не содердит число 2

# is_odd = f[0] %2 == 0 # находим первый элемент списка и проверяем остаток от деления на 2 равен ли 0
# print(is_odd)
# is_odd = not f[0] %2 # более правильная запись предыдущего варианта
# print(is_odd)

# username = input ('введите имя: ')
# if (username == 'Маша'):
#     print('Ура, это Маша')
# else:
#     print('Привет,', username)

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# username = input ('введите имя: ')
# if (username == 'Маша'):
#     print('Ура, это Маша')
# elif (username == 'Марина'):
#     print('Я так вас ждал, Марина')
# elif (username == 'Саша'):
#     print('Зравствуй, Саша')
# else:
#     print('Привет,', username)

# original = 23
# inverted = 0
# while original !=0:
#     inverted = inverted * 10 + (original % 10)
#     original // 10
# print(inverted)

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
#     print(original)
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(inverted)

# for i in 1,2,3,4,5:
#     print(i**2)

# list = [1,2,3,4,10,5]
# for i in list:
#     print(i)

# r = range(10)
# for i in r:
#     print(i)

# for i in range(1, 10, 2):
#     print(i)

# for i in 'qwe - rt y':
#     print(i)

text = 'съешь еще этих мягких французских булок'
# print(len(text)) # 39
# print('от' in  text) # True
# print(text.isdigit()) # False
# print(text.islower()) # True
# print(text.replace('еще', 'опять'))
# for c in text:
#     print(c)

# help(text.istitle)
# help(int)

# print(text[0])              # выводит с
# print(text[1])              # выводит ъ
# #print(text[len(text)])     # IndexError: string index out of range, так как индексация начинается с 0, правильно: print(len(text))
# print(text[len(text)-1])    # символ к, так как считает с конца строки
# print(text[-5])             # символ б
# print(text[:])              # символы от первого до последнего, иначе print(text)
# print(text[:2])             # символы съ (от 0 до 2 символа)
# print(text[len(text)-2:])   # ок
# print(text[2:9])            # ешь еще
# print(text[6:-18])          # еще этих мягких (от 6 до -18 символа)
# print(text[0:len(text):2])  # каждый второй символ "сеьееэи якхфацзкхблк"
# print(text[::5])              # каждый пятый символсеикакл "с эмхнку"
# text = text[2:9] + ' ' + text[-4] + ' ' + text[:2] # ешь еще у съ
# print(text)
