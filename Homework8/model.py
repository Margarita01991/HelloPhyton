# Model (изменение, поиск)

def select_mode():
    print('Режимы работы с данными:')
    print('1. Внесение данных\n\
2. Поиск данных\n\
3. Вывод данных\n\
4. Редактирование данных\n\
0. Выход из программы')
    mode = int(input('Выберите режим работы с данными => '))
    return mode

def get_contact():
    id = input('Введите данные сотрудника: ID => ')
    name = input('Фамилия, Имя => ')
    phone = input('Номер телефона => ')
    post = input('Должность => ')
    cost = input('Заработная плата => ')
    data = f'{id} || {name} || {phone} || {post} || {cost}\n'
    return data

def data_search(f):
    a = input('Введите данные для поиска: ')
    data = list(filter(lambda x: a in x, f.split('\n')))
    b = '\n'.join(data)
    return b

def editing_data(s):
    f = list(filter(lambda x: '||' not in x, s.split('||')))
    print('Выберите индекс элемента для редактирования:\n\
ID                0\n\
фамилия,имя       1\n\
номер телефона    2\n\
должность         3\n\
заработная плата  4')
    check = int(input('=> '))
    new_set = input('Введите новое значение:  ')
    f[check] = f' {new_set} '
    new_data = '||'.join(f)
    return new_data

def correct_search(r):
    book = data_search(r)
    print(book)
    while book.count('\n') > 0:
        print('Уточните критерии поиска')
        book = data_search(book)
        print(book)
    return book