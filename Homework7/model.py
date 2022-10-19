def get_contact():
    last_name = input('Enter lastname: ')
    first_name = input('Enter firstname: ')
    phone = input('Enter phone: ')
    return f'{last_name}||{first_name}||{phone} \n'

def find_contact(book,req):# (book:list,req: str) -> str:
    a = ''
    for i in book:
        if i.find(req) != -1:
            a = i
    if a == '':
        return 'Empty'
    else:
        return a

def get_request():
    return input('Contact to find: ')

def choose_mode():
    return int(input('MODE WRITING - 1; MODE FIND - 2; MODE PRINT - 3 '))

def print_data():
        with open('book.txt', 'r', encoding ='utf8') as f:
            text = f.read()
        print('Last name||First name||Phone')
        print(''.join(map(str, text)))
