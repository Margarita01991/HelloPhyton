
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler
from game import *

app = ApplicationBuilder().token("").build()

app.add_handler(CommandHandler("Hi", hi_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("start", start_command))
app.add_handler(CommandHandler("s", game_command))

print('server start')
app.run_polling()