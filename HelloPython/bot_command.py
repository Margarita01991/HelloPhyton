from config import *
from aiogram import *
from pytube import YouTube

bot=Bot(token=TOKEN)
dp=Dispatcher(bot=bot)

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
        await bot.send_message(chat_id, f'Загружаю: {yt.title}\n'
                                        f'С канала: [{yt.author}]({yt.channel_url})')
        await downland_video(url,message,bot)
        
async def downland_video(url,message,bot):
    yt = YouTube(url)
    yt.streams.filter(res="360p", file_extension="mp4").first().download(filename=f"name.mp4")
    print(yt.title)

        
if __name__ == '__main__':
    executor.start_polling(dp)    