import os
import sys
import telebot
from telebot import types

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from api import load_data
from bot import config, templates

bot = telebot.TeleBot(config.BOT_TOKEN)


@bot.message_handler(commands=['start'])
def startBot(message: types.Message):
    """
    Стартовое справочное сообщение
    """
    first_message = templates.start_message.format(
        user_first_name=message.from_user.first_name
    )
    sended_message = bot.send_message(
        message.chat.id, first_message, parse_mode="html"
    )
    bot.register_next_step_handler(sended_message, weaver)

@bot.message_handler(content_types=['text'])
def weather_location(message: types.Message):
    """
    Регулярные сообщения о погоде на завтрашний день
    """
    weaver(message)

def weaver(message: types.Message):
    """
    Функция, формумирующая экземпляр сообщения
    погодной сводки на завтрашний день
    """
    weather_data = load_data.get_middle_data(
        f"{config.WEATHER_DATA_URL}/weathertomorrow", 
        params={ "location": message.text }
    )
    if weather_data.get("error"):
        response_message = templates.error_weather_api_message\
            .format(**weather_data)

    else: 
        response_message = templates.weather_message\
            .format(**weather_data.get("data", {}))
        
    bot.send_message(
        message.chat.id, text=response_message, parse_mode="html"
    )


bot.infinity_polling()
