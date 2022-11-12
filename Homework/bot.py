import os
from config import *
from aiogram import *
from pytube import YouTube

bot=Bot(token=TOKEN)
dp=Dispatcher(bot=bot)

@dp.message_handler(commands=['start', 'help'])
async def start_message(message:types.Message):
    chat_id = message.chat.id

    await bot.send_message(chat_id, 'Привет, введи ссылку на видео с Youtube')

@dp.message_handler()

async def text_message(message:types.Message):
    chat_id = message.chat.id
    url = message.text
    yt = YouTube(url)
    if message.text.startswith == 'https://youtu.be/' or 'https://www.youtube.com/':
        await bot.send_message(chat_id, f'Загружаю: {yt.title}\n'
                                        f'С канала: [{yt.author}]({yt.channel_url})')
        await dowland_youtube_video(url,message,bot)
        
async def dowland_youtube_video(url,message,bot):
    yt = YouTube(url)
    stream = yt.streams.filter(progressive = True , file_extension='mp4')
    stream.get_highest_resolution().download(f'{message.chat.id}',f'{message.chat.id}_{yt.title}')
    with open (f'{message.chat.id}/{message.chat.id}_{yt.title}','rb') as video:
        await bot.send_video(message.chat.id,video,caption='@qwe123bot_bot')
        os.remove(f'{message.chat.id}/{message.chat.id}_{yt.title}')
        
if __name__ == '__main__':
    executor.start_polling(dp)    
