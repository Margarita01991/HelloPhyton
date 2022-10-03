# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'w')
# data.writelines(colors) # разделителей не будет
# data.close()

# exit()

# чтение файла
path = 'file.txt'
data = open(path,'r')
for line in data:
    print (line)
data.close()
