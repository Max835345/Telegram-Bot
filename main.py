# import moviepy.editor
# from pathlib import Path
#
# video_file = Path('Miyagi & Эндшпиль - Половина моя (Ｓｌｏｗｅｄ + Ｒｅｖｅｒｂ).mp4')
#
# video = moviepy.editor.VideoFileClip(f'{video_file}')
# audio = video.audio
# audio.write_audiofile(f'{video_file}.mp3')

# import time
# import logging
# from aiogram import Bot, Dispatcher,executor,types
#
# TOKEN = '5878447091:AAEOReeQ57nJlH0tdlEXJSUznAij0kgWrkI'
# MSG = "{}"
#
# bot = Bot(token=TOKEN)
# dp = Dispatcher(bot=bot)
#
# @dp.message_handler(commands=['start'])
# async def start_handler(message: types.Message):
#     user_id = message.from_user.id
#     user_name = message.from_user.first_name
#     user_full_name = message.from_user.full_name
#     logging.info(f'{user_id} {user_full_name} {time.asctime()}')
#
#     await message.reply(f'Привет, {user_full_name}!')
#
#     for i in range(10):
#         time.sleep(2)
#
#         await bot.send_message(user_id,MSG.format(user_name))
#
# if __name__ == '__main__':
#     executor.start_polling(dp)

# num = 9**8+3**5-9
# base = int(input("Base (2-9): "))
# if not(2 <= base <= 9):
#     quit()
#
# new_num = ''
#
# while num > 0:
#     new_num = str(num % base) + new_num
#     num //= base
#
# print(new_num)

import requests
import moviepy.editor
from pathlib import Path

video_url = 'https://youtu.be/6-qi5K-CDN0'
name = input()


def download_video(url=''):
    try:
        response = requests.get(url=url)

        with open(f'{name}.mp4', 'wb') as file:
            file.write(response.content)
        return 'Video successfully downloaded!'

    except Exception as _ex:

        return 'Upssss.......Check url'


def main():
    print(download_video(video_url))


if __name__ == '__main__':
    main()

video_file = Path(f'{name}.mp4')
video = moviepy.editor.VideoFileClip(f'{video_file}')
audio = video.audio
audio.write_audiofile(f'{video_file}.mp3')
