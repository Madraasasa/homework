# -*- coding: utf-8 -*-
import config
import random
import telebot
import os
import zipfile
from PIL import Image

bot = telebot.TeleBot("ВАШ ТОКЕН")
answers=['подтверждаю', 'угу' , 'не подтверждаю']
filename=[]
start_text='''Царь позвал к себе Иванушку-дурака и говорит:
    – Если завтра не принесешь двух говорящих птиц – голову срублю.
    Иван принес филина и воробья. Царь говорит:
    – Ну, пусть что-нибудь скажут.
    Иван спрашивает:
    – Воробей, почем раньше водка в магазине была?
    Воробей:
    – Чирик.
    Иван филину:
    – А ты, филин, подтверди.
    Филин:
    – Подтверждаю.'''
@bot.message_handler(commands=["start"])
def handle_start(message):

    bot.send_message(message.chat.id, start_text)
@bot.message_handler(commands=["finish"])
def handle_start(message):
    z = zipfile.ZipFile('stickers.zip', 'w')
    for file in filename:
        z.write(file)
    z.close()
    print('Архив сохранен ')
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, random.choice(answers))
@bot.message_handler(content_types=["sticker"])
def handle_text(message):
    bot.send_message(message.chat.id, 'Стикер сохранен, отправьте следующий или нажмите /finish')
    bot.send_sticker(message.chat.id, message.sticker.file_id)
    aaa=bot.get_file(message.sticker.file_id)

    print(aaa)
    aa=bot.download_file(aaa.file_path)
    b = open(aaa.file_path[9:], 'wb')

    b.write(aa)
    im = Image.open(aaa.file_path[9:]).convert("RGB")
    b.close()
    size=len(aaa.file_path[9:])
    print(aaa.file_path[9:size])
    im.save(aaa.file_path[9:size+5]+'png', "png")
    filename.append(aaa.file_path[9:size+5]+'png')
    print(message.sticker.emoji)
    os.remove(aaa.file_path[9:])



if __name__ == '__main__':
    bot.polling()

