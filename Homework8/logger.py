def write_new(a):
    with open('base.txt', 'a', encoding = 'utf-8') as f:
        f.write(f'{a}')
    print('Данные записаны')
    print()

def read_data():
    with open('base.txt', 'r', encoding = 'utf-8') as f:
        return f.read()

import os

def refining(book, new_book):
    with open('base.txt', 'r', encoding = 'utf-8') as f1, open('%s.bak' % 'base.txt', 'w', encoding = 'utf-8') as f2:
        for line in f1:
            if book in line:
                line = line.replace(book, new_book)
            f2.write(line)
    os.remove('base.txt')
    os.rename('%s.bak' % 'base.txt', 'base.txt')
    print('Данные отредактированы')
    print()