#  Скачивание видео из YouTube по ссылке(и дальнейшая его отправка пользователю) (https://pypi.org/project/pytube/)

import os
import logging
from config import * # файл с токеном удалила
from aiogram import *
from pytube import YouTube

bot=Bot(token=TOKEN)
dp=Dispatcher(bot=bot)
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands=['start'])
async def start_message(message:types.Message):
    chat_id = message.chat.id

    await bot.send_message(chat_id, 'Привет, введи ссылку на видео с Youtube')

@dp.message_handler()

async def text_message(message:types.Message):
    chat_id = message.chat.id
    url = message.text
    yt = YouTube(url)
    if message.text.startswith == 'https://youtu.be/' or 'https://www.youtube.com/':
        await bot.send_message(chat_id, f'Загружаю: {yt.title}\nС канала: [{yt.author}]({yt.channel_url})')
        await download_youtube_video(url,message,bot)
    else:
        await bot.send_message.reply(chat_id, "Напишите правильную команду")
        
async def download_youtube_video(url,message,bot):
    yt = YouTube(url)
    stream = yt.streams.filter(progressive = True , file_extension='mp4')
    stream.get_highest_resolution().download(f'{message.chat.id}',f'{message.chat.id}_{yt.title}')
    with open (f'{message.chat.id}/{message.chat.id}_{yt.title}','rb') as video:
        await bot.send_video(message.chat.id,video)
        os.remove(f'{message.chat.id}/{message.chat.id}_{yt.title}')
        
if __name__ == '__main__':
    executor.start_polling(dp)
