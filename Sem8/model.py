# Model (изменение, поиск)

# функция выбора режима работы
def selection_mode():
    print('Режимы работы с данными:')
    print('1. Внесение данных\n\
2. Поиск данных\n\
3. Вывод данных\n\
4. Редактирование данных\n\
0. Выход из программы')
    mode = int(input('Выберите режим работы с данными => '))
    return mode

# функция внесения данных нового сотрудника
def add_new_data():
    id = input('Введите данные сотрудника: ID => ')
    name = input('Фамилия, Имя => ')
    phone = input('Номер телефона => ')
    post = input('Должность => ')
    cost = input('Заработная плата => ')
    data = f'{id} || {name} || {phone} || {post} || {cost}\n'
    return data

# функция поиска данных сотрудника
def data_search(f):
    a = input('Введите данные для поиска: ')
    data = list(filter(lambda x: a in x, f.split('\n')))
    b = '\n'.join(data)
    return b

# функция редактирования данных
def editing_data(s):
    f = list(filter(lambda x: '||' not in x, s.split('||')))
    print('Выберите индекс элемента для редактирования:\n\
ID               -> 0\n\
фамилия,имя      -> 1\n\
номер телефона   -> 2\n\
должность        -> 3\n\
заработная плата -> 4')
    check = int(input('=> '))
    print(f'Текущее значение элемента -> {f[check]}')
    new_value = input('Введите новое значение элемента -> ')
    f[check] = f' {new_value} '
    new_data = '||'.join(f)
    return new_data

# функция проверки корректного поиска
def correct_search(r):
    old_str = data_search(r)
    print(old_str)
    while old_str.count('\n') > 0:
        print('Уточните критерии поиска, чтобы получить запись конкретного сотрудника')
        old_str = data_search(old_str)
        print(old_str)
    return old_str