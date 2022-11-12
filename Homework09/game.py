from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from random import randint
import time
import emoji

async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hi {update.effective_user.first_name}!\nДля начала игры введите команду **/start**')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Введите команду: /start\n')

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'''На столе лежит {balance[-1]} конфет.\nИграют два игрока делая ход друг после друга.\nПервый ход определяется жеребьёвкой.\n
За один ход можно забрать не более чем 28 конфет.\nВсе конфеты оппонента достаются сделавшему последний ход.''')
    await update.message.reply_text(f'{emoji.emojize("Случайный выбор первого хода..... :eight_o’clock: :eight-thirty: :five_o’clock:")}')
    time.sleep(4)
    play = randint(1,2)

    if play==1:
        await update.message.reply_text(f'Первым ходит {update.effective_user.first_name}')
        await update.message.reply_text('Набери /s и количество конфет')
    else:
        await update.message.reply_text('Первым хожу я')
        y = randint(1, 28)
        await update.message.reply_text(f'Я беру {y} конфет')
        b = balance[len(balance) - 1]
        b -= y
        balance.append(b)
        await update.message.reply_text(f'На столе осталось {b} конфет\nНабери /s и количество конфет')

balance = [100]

async def game_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    b = balance[len(balance) - 1]
    msg = update.message.text
    items = msg.split()
    a = int(items[1])
    if a > 28:
        await update.message.reply_text(f'Необходимо взять не более 28 конфет')
    else:
        b -= a
        await update.message.reply_text(f'Ты взял {a} конфет.\nНа столе осталось {b} конфет')
        balance.append(b)
        print(balance)
        if b <= 0:
            await update.message.reply_text(f'{update.effective_user.first_name} {emoji.emojize("выиграл :1st_place_medal:")}')
        else:
            if b > 28:
                y = randint(1, 28)
                await update.message.reply_text(f'Я беру {y} конфет')
                b -= y
                await update.message.reply_text(f'На столе осталось {b} конфет\nНабери /s и количество конфет')
            else:
                await update.message.reply_text(f'Я беру {b} конфет.\n{update.effective_user.first_name} {emoji.emojize("проиграл :crying_face:")}')
    balance.append(b)
    while balance[-1] <= 0:
        balance.append(100)