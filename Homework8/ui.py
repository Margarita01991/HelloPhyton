import model
import logger

while True:
    mode = model.select_mode()
    if mode == 1: 
        logger.write_new(model.get_contact())
    
    elif mode == 2: 
        print(model.data_search(logger.read_data()))

    elif mode == 3: 
        print(logger.read_data())

    elif mode == 4: 
        book = model.correct_search(logger.read_data())
        new_book = model.editing_data(book)
        logger.refining(book, new_book)

    elif mode == 0: 
        print('Работа закончена.')
        break
    
    else:
        print('Введена неверная команда. Повторите ввод.')
