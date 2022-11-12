import random
import matplotlib.pyplot as plt 

count = 312
x = list(range(1, 7))
y = [0 for i in x]

fig, ax = plt.subplots()

for _ in range (count):
    y[random.randint(0,5)] += 1

ax.bar(x,y)

y.sort()

stat = [f'{i+1}: {round(y[i] / count * 100)}%' for i in range(0,6)]
print (stat)

# plt.show()

