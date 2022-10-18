def get_contact():
    name = input('NAME: ')
    phone = input('PHONE: ')
    return f'{name}||{phone} \n'

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
    return int(input('MODE WRITING - 1; MODE FIND - 2: '))
