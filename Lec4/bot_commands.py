from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import datetime
from spy import *
import emoji

async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'Hi {update.effective_user.first_name}!')

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'{datetime.now().time()}')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'/hi\n/time\n/help\n/sum')

async def popa_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'ты опять в своем репертуаре, {update.effective_user.first_name}! ')

async def pupsik_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'{emoji.emojize("i love YOU :red_heart:", variant="emoji_type")}')

async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text # кладем сообщение от пользователя в отдельную переменную
    print(msg) # эхобот
    items = msg.split() # добавляем сообщение в список с разделителем пробел: (/sum 123 232453) - три элемента sum и 2 числа
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x}+{y}={x+y}')