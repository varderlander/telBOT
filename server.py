import telebot
import requests
import os
import urllib
import time
from config import main_token
import random
from telebot import types
import emoji
from bs4 import BeautifulSoup


#photo URL
# url='http://scontent-b.cdninstagram.com/hphotos-xfa1/t51.2885-15/e15/10919672_584633251672188_179950734_n.jpg'
# f = open('test.jpg','wb')
# f.write(urllib.request.urlopen(url).read())
# f.close()


bot = telebot.TeleBot(main_token)

@bot.message_handler(content_types=['sticker']) #ID sticker
def stickers_get_id(message): 
    print(message)

def main():
    markup = types.ReplyKeyboardMarkup(True)
    item = types.KeyboardButton("🎲 Рандомное число")
    item_weather = types.KeyboardButton('📰 Новости')
    item_photo_main = types.KeyboardButton('📷 Получить фото')
    # item_video_main = types.KeyboardButton('📽 Видео')
    item_clear_buttons = types.KeyboardButton('❌ Убрать кнопки')
    item_weather_button = types.KeyboardButton('☔️ Погода')

    
    markup.add(item, item_weather, item_weather_button)
    markup.add(item_photo_main, item_clear_buttons) #item_video_main

    return markup


def for_news():
    markup = types.ReplyKeyboardMarkup(True)
    button_weather1 = types.KeyboardButton('Спорт ↕️')
    button_weather2 = types.KeyboardButton('📺 Политика')
    button_weather3 = types.KeyboardButton('Наука ↕️')
    button_weather4 = types.KeyboardButton('🚨 Происшествия')
    button_weather5 = types.KeyboardButton('🏙 Общество')
    button_weather6 = types.KeyboardButton('💵 Экономика')
    button_weather7 = types.KeyboardButton('◀️ Назад')
    button_weather8 = types.KeyboardButton('❗️ Другое')
 
    markup.add(button_weather1, button_weather2, button_weather3)
    markup.add(button_weather4, button_weather5, button_weather6)
    markup.add(button_weather8 ,button_weather7)
    return markup

def for_sport():
    sport_but = types.ReplyKeyboardMarkup(True)
    button_sport1 = types.KeyboardButton('⚽️ Футбол')
    button_sport2 = types.KeyboardButton('🏒 Хоккей')
    button_sport3 = types.KeyboardButton('🤼‍♂️ Единоборства')
    button_sport4 = types.KeyboardButton('🏀 Баскетбол')
    button_sport5 = types.KeyboardButton('🎾 Теннис')
    button_sport6 = types.KeyboardButton('⛷ Лыжи')
    button_sport7 = types.KeyboardButton('◀️ Обратно к новостям')

    sport_but.add(button_sport1, button_sport2, button_sport3)
    sport_but.add(button_sport4, button_sport5, button_sport6)
    sport_but.add(button_sport7)
    return sport_but

def for_science():
    science_but = types.ReplyKeyboardMarkup(True)
    button_science1 = types.KeyboardButton('🚀 Космос')
    button_science2 = types.KeyboardButton('💖 Здоровье')
    button_science3 = types.KeyboardButton('🛠 Технологии')
    button_science4 = types.KeyboardButton('🧬 Генетика')
    button_science5 = types.KeyboardButton('Ⓜ️ Математика')
    button_science6 = types.KeyboardButton('👬 Социология')
    button_science7 = types.KeyboardButton('◀️ Обратно к новостям')

    science_but.add(button_science1, button_science2, button_science3)
    science_but.add(button_science4, button_science5, button_science6)
    science_but.add(button_science7)
    return science_but



def another():
    markup1 = types.InlineKeyboardMarkup(row_width=2)
    item2 = types.InlineKeyboardButton('Еще раз?', callback_data='again')

    markup1.add(item2)
    return markup1

def delete_buttons():
    key_delete = types.InlineKeyboardMarkup(row_width=2)
    delete_yes = types.InlineKeyboardButton('Да', callback_data='yes_delete')
    delete_no = types.InlineKeyboardButton('Нет', callback_data='no_delete')

    key_delete.add(delete_yes, delete_no)
    return key_delete


def how_are_you():
    KeyBRD = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton('Хорошо', callback_data='good')
    item2 = types.InlineKeyboardButton('Не очень', callback_data='bad')

    KeyBRD.add(item1, item2)
    return KeyBRD


@bot.message_handler(commands=['video'], content_types=['text']) #/video (доработать)
def video(message):
    if message.text.lower() == '/video':
        bot.send_message(message.chat.id, 'Нажми на кнопочную форму, чтобы получить видео!', reply_markup=main())

@bot.message_handler(commands=['photo'], content_types=['text']) #/photo
def photo(message):
    if message.text.lower() == '/photo':
        bot.send_message(message.chat.id, 'Нажмите на кнопку ниже, чтобы получить фотографию.', reply_markup=main())

@bot.message_handler(commands=['bye']) #команда /bye
def bye(message):
    bot.send_message(message.chat.id, f'Уже уходишь? До скорой встречи!', reply_markup=types.ReplyKeyboardRemove())
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAID_GBnVAUCbG2RR8lRszX7zCsbqs8cAAJSAANBtVYMAhDiZGl_D3IeBA')

@bot.message_handler(commands=['start']) #команда /start
def start(message):
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAID9mBnUZt4NxMPcksv0J_jA7oSx1LOAAJUAANBtVYMarf4xwiNAfoeBA')
    bot.send_message(message.chat.id, f'Я бот. Приятно познакомиться, пропиши /help и ты узнаешь что я умею!', reply_markup=main())

@bot.message_handler(commands=['help']) #команда /help
def help(message):
    bot.send_message(message.chat.id, f'Пропиши /weather, /news, или посмотри на кнопки :)', reply_markup=main())


@bot.message_handler(commands=['news'], content_types=['text']) #команда /news
def handle(message):
    URL = 'https://ria.ru/world/'

    headers = {
        'User_Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 YaBrowser/21.2.4.172 Yowser/2.5 Safari/537.36'
    }

    response = requests.get(URL, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    texts = soup.findAll('a', 'list-item__title')

    for i in range(0, len(texts[:-15])):
        txt = str(i + 1) + ') ' + texts[i].text
        bot.send_message(message.chat.id, '<a href="{}"> {}</a>'.format(texts[i]['href'], txt), parse_mode='html')

@bot.message_handler(commands=['weather'], content_types=['text']) #команда /weather 
def weather(message):
    bot.send_message(message.chat.id, f'Напиши город, в котором хочешь узнать погоду', reply_markup=main())
    bot.register_next_step_handler(message, get_weather)

@bot.message_handler(commands=['weather'], content_types=['text'])
def get_weather(message):
        global city_name
        city_name = message.text
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=a039ce0930b5de27ee7f762203915016'.format(city_name)
        
        try:
            params = {'units': 'metric', 'lang': 'ru'}
            result = requests.get(url, params=params)
            weather = result.json()


            if weather["main"]['temp'] < 10:
                status = "Сейчас холодно!"
            elif weather["main"]['temp'] < 20:
                status = "Сейчас прохладно!"
            elif weather["main"]['temp'] > 38:
                status = "Сейчас жарко!"
            else:
                status = "Сейчас отличная температура!"

            bot.send_message(message.chat.id, "В городе " + str(weather["name"]) + " температура " + str(float(weather["main"]['temp'])) + '🌡' + "\n" + 
                    "Максимальная температура " + str(float(weather['main']['temp_max'])) + "\n" + 
                    "Минимальная температура " + str(float(weather['main']['temp_min'])) + "\n" + 
                    "Скорость ветра " + str(float(weather['wind']['speed'])) + ' 🌪' +"\n" + 
                    "Давление " + str(float(weather['main']['pressure'])) + ' ⚰️' + "\n" + 
                    "Влажность " + str(int(weather['main']['humidity'])) + "%" + ' 💦' + "\n" + 
                    "Видимость " + str(weather['visibility']) + ' 👀' +"\n\n" + status)
                    # "Описание " + str(weather['weather'][0]["description"]) + "\n\n" + status)
        except:
            bot.send_message(message.chat.id, "Город " + city_name + " не найден")

name = ''
surname = ''
age = 0

@bot.message_handler(commands=['reg'], content_types=['text']) #команда /reg
def get_user(message):
    if message.text == '/reg':
        bot.send_message(message.chat.id, 'Сколько тебе лет?')
        bot.register_next_step_handler(message, get_age)
    else:
        bot.send_message(message.chat.id, 'Напиши /reg')

# @bot.message_handler(commands=['reg'], content_types=['text'])
# def get_name(message):
#     global name
#     bot.send_message(message.chat.id, 'Какая у тебя фамилия?')
#     bot.register_next_step_handler(message, get_surname)

# @bot.message_handler(commands=['reg'], content_types=['text'])
# def get_surname(message):
#     global surname
#     bot.send_message(message.chat.id, 'Сколько тебе лет?')
#     bot.register_next_step_handler(message, get_age)


# @bot.message_handler(commands=['game']) #вставка игры (t-rex), /game
# def game_short_name(message):
#     bot.send_game(chat_id=message.chat.id, game_short_name='Sologame')


# @bot.callback_query_handler(func=lambda callback_query: callback_query.game_short_name == 'Sologame')
# def game(call):
#     bot.answer_callback_query(callback_query_id=call.id, url='http://www.trex-game.skipser.com/')


def get_age(message):
    global age
    while age == 0:
        try:
            age = int(message.text)
        except Exception:
            bot.send_message(message.chat.id, 'Цифрами пожалуйста!!!')

        keyboard = types.InlineKeyboardMarkup(row_width=2)
        key_yes = types.InlineKeyboardButton(text='Верно', callback_data='yes')
        key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
        keyboard.add(key_yes, key_no)
        question = 'Спасибо, я запомню, что тебе ' + str(age) + ' лет' + '!'


        bot.send_message(message.chat.id, text=question,  reply_markup=keyboard) #доработать name, surname





@bot.message_handler(content_types=['text']) #вывод и ответ бота на сообщения 
def get_text_message(message):
    if message.text.lower() == 'привет':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAID9mBnUZt4NxMPcksv0J_jA7oSx1LOAAJUAANBtVYMarf4xwiNAfoeBA')
        bot.send_message(message.chat.id, 'Что ты хочешь увидеть?', reply_markup=main())
    
    
    # elif message.text.lower() == '📽 видео':                              ВИДЕО НЕ РАБОТАЕТ
    #     video = open('test/' + random.choice(os.listdir('video')), 'rb')
    #     bot.send_video(message.chat.id, video, caption='Вот твое видео!')
    
    elif message.text.lower() == '📷 получить фото':
        # bot.send_chat_action(message.chat.id, 'Посмотреть фото')          НЕ РАБОТАЕТ
        # img = open('test.jpg', 'rb')
        # bot.send_photo(message.chat.id, img, reply_to_message_id=message.message_id)
        # img.close()
        photo = open('test/' + random.choice(os.listdir('test')), 'rb')
        bot.send_photo(message.chat.id, photo, caption = 'Лови фотографию!')
    
    elif message.text.lower() == '🎲 рандомное число':
        bot.send_message(message.chat.id, str(random.randint(0,100)), reply_markup=another())

    elif message.text.lower() == '❌ убрать кнопки':
        bot.send_message(message.chat.id, 'Ты уверен?', reply_markup=delete_buttons())
    
    elif message.text.lower() == '❗️ другое':
        URL = 'https://ria.ru/category_kino/'

        headers = {
        'User_Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 YaBrowser/21.2.4.172 Yowser/2.5 Safari/537.36'
        }

        response = requests.get(URL, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        texts = soup.findAll('a', 'list-item__title')

        for i in range(0, len(texts[:-19])):
            txt = str(i + 1) + '. ' + texts[i].text
            bot.send_message(message.chat.id, '<a href="{}"> {}</a>'.format(texts[i]['href'], txt), parse_mode='html')

        URL = 'https://ria.ru/tourism_visual/'

        # headers = {
        # 'User_Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 YaBrowser/21.2.4.172 Yowser/2.5 Safari/537.36'
        # }

        response = requests.get(URL, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        texts = soup.findAll('a', 'list-item__title')

        for i in range(len(texts[:-14]), 0, -1):
            txt = str(i + 1) + '. ' + texts[i].text
            bot.send_message(message.chat.id, '<a href="{}"> {}</a>'.format(texts[i]['href'], txt), parse_mode='html')

        URL = 'https://ria.ru/category_religiya/'

        # headers = {
        # 'User_Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 YaBrowser/21.2.4.172 Yowser/2.5 Safari/537.36'
        # }

        response = requests.get(URL, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        texts = soup.findAll('a', 'list-item__title')

        for i in range(len(texts[:-18]), 1, -1):
            txt = str(i + 1) + '. ' + texts[i].text
            bot.send_message(message.chat.id, '<a href="{}"> {}</a>'.format(texts[i]['href'], txt), parse_mode='html')

        URL = 'https://ria.ru/defense_safety/'

        # headers = {
        # 'User_Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 YaBrowser/21.2.4.172 Yowser/2.5 Safari/537.36'
        # }

        response = requests.get(URL, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        texts = soup.findAll('a', 'list-item__title')

        for i in range(len(texts[:-17]), 2, -1):
            txt = str(i + 1) + '. ' + texts[i].text
            bot.send_message(message.chat.id, '<a href="{}"> {}</a>'.format(texts[i]['href'], txt), parse_mode='html')

        
        URL = 'https://ria.ru/world/'

        # headers = {
        # 'User_Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 YaBrowser/21.2.4.172 Yowser/2.5 Safari/537.36'
        # }

        response = requests.get(URL, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        texts = soup.findAll('a', 'list-item__title')

        for i in range(len(texts[:-16]), 3, -1):
            txt = str(i + 1) + '. ' + texts[i].text
            bot.send_message(message.chat.id, '<a href="{}"> {}</a>'.format(texts[i]['href'], txt), parse_mode='html')
        

    elif message.text.lower() == '📺 политика':
        URL = 'https://ria.ru/politics/'

        headers = {
        'User_Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 YaBrowser/21.2.4.172 Yowser/2.5 Safari/537.36'
        }

        response = requests.get(URL, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        texts = soup.findAll('a', 'list-item__title')

        for i in range(0, len(texts[:-15])):
            txt = str(i + 1) + '. ' + texts[i].text
            bot.send_message(message.chat.id, '<a href="{}"> {}</a>'.format(texts[i]['href'], txt), parse_mode='html')

    elif message.text.lower() == '🚨 происшествия':
        URL = 'https://ria.ru/incidents/'

        headers = {
        'User_Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 YaBrowser/21.2.4.172 Yowser/2.5 Safari/537.36'
        }

        response = requests.get(URL, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        texts = soup.findAll('a', 'list-item__title')

        for i in range(0, len(texts[:-15])):
            txt = str(i + 1) + '. ' + texts[i].text
            bot.send_message(message.chat.id, '<a href="{}"> {}</a>'.format(texts[i]['href'], txt), parse_mode='html')

    elif message.text.lower() == '🏙 общество':
        URL = 'https://ria.ru/society/'

        headers = {
        'User_Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 YaBrowser/21.2.4.172 Yowser/2.5 Safari/537.36'
        }

        response = requests.get(URL, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        texts = soup.findAll('a', 'list-item__title')

        for i in range(0, len(texts[:-7])):
            txt = str(i + 1) + '. ' + texts[i].text
            bot.send_message(message.chat.id, '<a href="{}"> {}</a>'.format(texts[i]['href'], txt), parse_mode='html')

    elif message.text.lower() == '💵 экономика':
        URL = 'https://ria.ru/economy/'

        headers = {
        'User_Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 YaBrowser/21.2.4.172 Yowser/2.5 Safari/537.36'
        }

        response = requests.get(URL, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        texts = soup.findAll('a', 'list-item__title')

        for i in range(0, len(texts[:-7])):
            txt = str(i + 1) + '. ' + texts[i].text
            bot.send_message(message.chat.id, '<a href="{}"> {}</a>'.format(texts[i]['href'], txt), parse_mode='html')

    elif message.text.lower() == '⚽️ футбол':
        URL = 'https://ria.ru/football/'

        headers = {
        'User_Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 YaBrowser/21.2.4.172 Yowser/2.5 Safari/537.36'
        }

        response = requests.get(URL, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        texts = soup.findAll('a', 'list-item__title')

        for i in range(0, len(texts[:-7])):
            txt = str(i + 1) + '. ' + texts[i].text
            bot.send_message(message.chat.id, '<a href="{}"> {}</a>'.format(texts[i]['href'], txt), parse_mode='html')

    elif message.text.lower() == '🏒 хоккей':
        URL = 'https://ria.ru/hockey/'

        headers = {
        'User_Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 YaBrowser/21.2.4.172 Yowser/2.5 Safari/537.36'
        }

        response = requests.get(URL, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        texts = soup.findAll('a', 'list-item__title')

        for i in range(0, len(texts[:-7])):
            txt = str(i + 1) + '. ' + texts[i].text
            bot.send_message(message.chat.id, '<a href="{}"> {}</a>'.format(texts[i]['href'], txt), parse_mode='html')

    elif message.text.lower() == '🤼‍♂️ единоборства':
        URL = 'https://ria.ru/fights/'

        headers = {
        'User_Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 YaBrowser/21.2.4.172 Yowser/2.5 Safari/537.36'
        }

        response = requests.get(URL, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        texts = soup.findAll('a', 'list-item__title')

        for i in range(0, len(texts[:-7])):
            txt = str(i + 1) + '. ' + texts[i].text
            bot.send_message(message.chat.id, '<a href="{}"> {}</a>'.format(texts[i]['href'], txt), parse_mode='html')

    elif message.text.lower() == '🏀 баскетбол':
        URL = 'https://ria.ru/basketball/'

        headers = {
        'User_Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 YaBrowser/21.2.4.172 Yowser/2.5 Safari/537.36'
        }

        response = requests.get(URL, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        texts = soup.findAll('a', 'list-item__title')

        for i in range(0, len(texts[:-7])):
            txt = str(i + 1) + '. ' + texts[i].text
            bot.send_message(message.chat.id, '<a href="{}"> {}</a>'.format(texts[i]['href'], txt), parse_mode='html')

    elif message.text.lower() == '🎾 теннис':
        URL = 'https://ria.ru/tennis/'

        headers = {
        'User_Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 YaBrowser/21.2.4.172 Yowser/2.5 Safari/537.36'
        }

        response = requests.get(URL, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        texts = soup.findAll('a', 'list-item__title')

        for i in range(0, len(texts[:-7])):
            txt = str(i + 1) + '. ' + texts[i].text
            bot.send_message(message.chat.id, '<a href="{}"> {}</a>'.format(texts[i]['href'], txt), parse_mode='html')

    elif message.text.lower() == '⛷ лыжи':
        URL = 'https://ria.ru/cross_country/'

        headers = {
        'User_Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 YaBrowser/21.2.4.172 Yowser/2.5 Safari/537.36'
        }

        response = requests.get(URL, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        texts = soup.findAll('a', 'list-item__title')

        for i in range(0, len(texts[:-15])):
            txt = str(i + 1) + '. ' + texts[i].text
            bot.send_message(message.chat.id, '<a href="{}"> {}</a>'.format(texts[i]['href'], txt), parse_mode='html')

    elif message.text.lower() == '🚀 космос':
        URL = 'https://ria.ru/space/'

        headers = {
        'User_Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 YaBrowser/21.2.4.172 Yowser/2.5 Safari/537.36'
        }

        response = requests.get(URL, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        texts = soup.findAll('a', 'list-item__title')

        for i in range(0, len(texts[:-15])):
            txt = str(i + 1) + '. ' + texts[i].text
            bot.send_message(message.chat.id, '<a href="{}"> {}</a>'.format(texts[i]['href'], txt), parse_mode='html')

    elif message.text.lower() == '💖 здоровье':
        URL = 'https://ria.ru/sn_health/'

        headers = {
        'User_Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 YaBrowser/21.2.4.172 Yowser/2.5 Safari/537.36'
        }

        response = requests.get(URL, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        texts = soup.findAll('a', 'list-item__title')

        for i in range(0, len(texts[:-10])):
            txt = str(i + 1) + '. ' + texts[i].text
            bot.send_message(message.chat.id, '<a href="{}"> {}</a>'.format(texts[i]['href'], txt), parse_mode='html')

    elif message.text.lower() == '🛠 технологии':
        URL = 'https://ria.ru/technology/'

        headers = {
        'User_Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 YaBrowser/21.2.4.172 Yowser/2.5 Safari/537.36'
        }

        response = requests.get(URL, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        texts = soup.findAll('a', 'list-item__title')

        for i in range(0, len(texts[:-15])):
            txt = str(i + 1) + '. ' + texts[i].text
            bot.send_message(message.chat.id, '<a href="{}"> {}</a>'.format(texts[i]['href'], txt), parse_mode='html')

    elif message.text.lower() == '🧬 генетика':
        URL = 'https://ria.ru/keyword_genetika/'

        headers = {
        'User_Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 YaBrowser/21.2.4.172 Yowser/2.5 Safari/537.36'
        }

        response = requests.get(URL, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        texts = soup.findAll('a', 'list-item__title')

        for i in range(0, len(texts[:-15])):
            txt = str(i + 1) + '. ' + texts[i].text
            bot.send_message(message.chat.id, '<a href="{}"> {}</a>'.format(texts[i]['href'], txt), parse_mode='html')

    elif message.text.lower() == 'Ⓜ️ математика':
        URL = 'https://ria.ru/keyword_matematika/'

        headers = {
        'User_Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 YaBrowser/21.2.4.172 Yowser/2.5 Safari/537.36'
        }

        response = requests.get(URL, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        texts = soup.findAll('a', 'list-item__title')

        for i in range(0, len(texts[:-15])):
            txt = str(i + 1) + '. ' + texts[i].text
            bot.send_message(message.chat.id, '<a href="{}"> {}</a>'.format(texts[i]['href'], txt), parse_mode='html')

    elif message.text.lower() == '👬 социология':
        URL = 'https://ria.ru/keyword_sociologija/'

        headers = {
        'User_Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 YaBrowser/21.2.4.172 Yowser/2.5 Safari/537.36'
        }

        response = requests.get(URL, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        texts = soup.findAll('a', 'list-item__title')

        for i in range(0, len(texts[:-15])):
            txt = str(i + 1) + '. ' + texts[i].text
            bot.send_message(message.chat.id, '<a href="{}"> {}</a>'.format(texts[i]['href'], txt), parse_mode='html')

    elif message.text.lower() == '📰 новости':
        bot.send_message(message.chat.id, 'Какие новости ты хочешь увидеть?', reply_markup=for_news())

    elif message.text.lower() == '☔️ погода':
        bot.send_message(message.chat.id, 'Чтобы узнать погоду, пропиши /weather', reply_markup=main())

    elif message.text.lower() == 'спорт ↕️':
        bot.send_message(message.chat.id, 'Какую категорию спорта ты хочешь видеть?', reply_markup=for_sport())
    
    elif message.text.lower() == 'наука ↕️':
        bot.send_message(message.chat.id, 'Какую категорию науки ты хочешь видеть?', reply_markup=for_science())

    elif message.text.lower() == '◀️ назад':
        bot.send_message(message.chat.id, 'Хорошо', reply_markup=main())

    elif message.text.lower() == '◀️ обратно к новостям':
        bot.send_message(message.chat.id, 'Окей', reply_markup=for_news())
    
    elif message.text.lower() == 'как дела?':
        bot.send_message(message.chat.id, 'Отлично, сам как?', reply_markup=how_are_you())
    
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'До скорой встречи!', reply_markup=types.ReplyKeyboardRemove())
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAID_GBnVAUCbG2RR8lRszX7zCsbqs8cAAJSAANBtVYMAhDiZGl_D3IeBA')

    else:
        bot.send_message(message.chat.id, 'Не понятно для меня :( Напиши /help для просмотра команд, которые я умею', reply_markup=main())


@bot.callback_query_handler(func=lambda call: call.data=='yes')
def calluser_age_yes(call):
    try:
        if call.data == 'yes':
            bot.send_message(call.message.chat.id, 'Запомню :)')

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Хорошо', reply_markup=None)

    except Exception as e:
       print(repr(e))

@bot.callback_query_handler(func=lambda call: call.data=='no')
def calluser_age_no(call):
    try:
        if call.data == 'no':
            bot.send_message(call.message.chat.id, 'Пропиши еще раз /reg') #доработать обратную функцию на ответ

            
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Упс...', reply_markup=None)
    

    except Exception as e:
       print(repr(e))


@bot.callback_query_handler(func=lambda call: call.data=='again')
def callback_inline(call):
    try:
        if call.data == 'again':
            bot.send_message(call.message.chat.id, str(random.randint(0,100)), reply_markup=main())

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Рандомное число', reply_markup=None)

            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Удачи")
    
    except Exception as e:
       print(repr(e))

@bot.callback_query_handler(func=lambda call: call.data=='good')
def callback_good(call):
    try:
        if call.data == 'good':
            bot.send_message(call.message.chat.id, 'Хорошего дня!', reply_markup=main())

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Вот и отлично :)', reply_markup=None)
    except Exception as e:
       print(repr(e))

@bot.callback_query_handler(func=lambda call: call.data=='yes_delete')
def callback_yes(call):
    try:
        if call.data == 'yes_delete':
            bot.send_message(call.message.chat.id, 'Хорошего дня!', reply_markup=types.ReplyKeyboardRemove())

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Хорошо', reply_markup=None)
    except Exception as e:
       print(repr(e))

@bot.callback_query_handler(func=lambda call: call.data=='no_delete')
def callback_no(call):
    try:
        if call.data == 'no_delete':
            bot.send_message(call.message.chat.id, 'Не трогаю я твои кнопки!', reply_markup=main())

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Хорошо-хорошо', reply_markup=None)
    except Exception as e:
       print(repr(e))

@bot.callback_query_handler(func=lambda call: call.data=='bad')
def callback_bad(call):
    try:
        if call.data == 'bad':
            bot.send_message(call.message.chat.id, 'Все будет хорошо!', reply_markup=main())

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Ничего страшного', reply_markup=None)
    
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="Не вешай нос")
    except Exception as e:
       print(repr(e))

bot.polling(none_stop=True)


while True:
    time.sleep()