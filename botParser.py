import telebot
from telebot import types
import random 
from bs4 import BeautifulSoup
import requests 
import fake_useragent

bot = telebot.TeleBot("5954735909:AAEtE9Yo-S1X3GEGycHcifIC5agVM_RktdE")


#/start
@bot.message_handler(commands=['start'])
def introduce(message):
	mess = "Привет, меня зовут <b>Гоша</b> и я могу рассказать пару анекдотов. Для этого жми на панель снизу или введи команду /joke" 
	markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
	button1 = types.KeyboardButton("Расскажи анекдот")
	button2 = types.KeyboardButton("/help")
	markup.add(button1, button2)
	bot.send_message(message.chat.id, mess, reply_markup = markup, parse_mode='html')
#/help
@bot.message_handler(commands=['help'])
def help(message):
	bot.send_message(message.chat.id, "Для того, чтоб получить шутку нажмите /joke")\
	
#joke
@bot.message_handler(commands = ['joke'])
def joke1 (message):
	user = fake_useragent.UserAgent().random
	header = {
		'user-agent': user
	}
	url = 'https://anekdotov.net/anekdot/'
	request = requests.get(url, headers = header).text
	soup = BeautifulSoup(request, 'lxml')
	anekdotes = soup.find_all('div', class_='anekdot')
	bot.send_message(message.chat.id, random.choice(anekdotes).text)


@bot.message_handler(content_types = ['text'])
def joke2 (message):
	if message.text == "Расскажи анекдот":
		user = fake_useragent.UserAgent().random
		header = {
			'user-agent': user
		}
		url = 'https://anekdotov.net/anekdot/'
		request = requests.get(url, headers = header).text
		soup = BeautifulSoup(request, 'lxml')
		anekdotes = soup.find_all('div', class_='anekdot')
		bot.send_message(message.chat.id, random.choice(anekdotes).text)
	else: 
		bot.send_message(message.chat.id, "Извините, я вас не понимаю")

bot.infinity_polling()


