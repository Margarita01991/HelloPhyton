# Создать информационную систему, позволяющую работать с некой компанией/студентами ВУЗа/учениками школы.
# import model

import model
import logger


while True:
    mode = model.selection_mode()
    if mode == 1: # вызов функции добавления данных
        logger.write_new_data(model.add_new_data())
    
    elif mode == 2: # вызов функции поиска данных
        print(model.data_search(logger.read_data()))

    elif mode == 3: # вызов функции вывода данных
        print(logger.read_data())

    elif mode == 4: # вызов функции редактирования данных
        old_str = model.correct_search(logger.read_data())
        new_str = model.editing_data(old_str)
        logger.alter(old_str, new_str)

    elif mode == 0: # выход
        print('Выход.')
        break
    
    else:
        print('Введите цифру от 0 до 3')