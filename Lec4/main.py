'''
from progress.bar import Bar
import time       # добавляем библиотеку таймера
bar = Bar('Processing', max=20)
for i in range(20):
    # Do some work
    time.sleep(1) # добавляем таймер 1 сек
    bar.next()
bar.finish()
'''
'''
import emoji
print(emoji.emojize('Python is :thumbs_up:'))
print(emoji.emojize("Python is fun :yellow_heart:", variant="emoji_type"))
# Python is fun ❤️ #red heart, not black heart
'''
'''
import matplotlib.pyplot as plt
import numpy as np
list = [1,2,3,2,7]
plt.plot(list)
plt.show()
'''

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *
import emoji


app = ApplicationBuilder().token("5641904902:AAHp26DbDpvJVjpQpZRrlD4BQ7R_Uunvcuk").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("popa", popa_command))
app.add_handler(CommandHandler("pupsik", pupsik_command))

print('server start')
app.run_polling()
