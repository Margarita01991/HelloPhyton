# 5. Реализуйте алгоритм перемешивания списка.

# list = [14, 'desert', 24.1, 'home', 0.12, 'three']
import random
list = [i for i in range(random.randint(3,6))]
print(list) 
random.shuffle(list)
print(list) 