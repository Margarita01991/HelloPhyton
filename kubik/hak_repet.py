import os
# Модуль time понадобится для паузы, чтобы не слишком часто открывалось
import time
# Создаем текстовый файл
f=open('beer.txt','w',encoding='UTF-8')
f.write('СРОЧНО НАЛЕЙТЕ ХАКЕРУ ПИВА, ИНАЧЕ ЭТО НЕ ЗАКОНЧИТСЯ!!')
f.close()
while True:
    # Открываем файл программой по умолчанию
    os.startfile('beer.txt')
    # Делаем паузу в одну секунду
    time.sleep(10)