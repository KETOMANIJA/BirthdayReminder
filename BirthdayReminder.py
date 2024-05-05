import telebot
from telebot import types
import datetime
import time

class BirthdayReminder:
    def __init__(self, name):
        self.name = name

    def remind(self):
        return f"Nepamiršk nusipirkti saldainių {self.name} gimtadieniui!"

def send_reminder(reminder):
    chat_id = 6080846508 
    bot.send_message(chat_id, reminder.remind())


bot = telebot.TeleBot('7197512209:AAEpax-QlHta4WByKsJHmYShw8OArbPNYZg')
chat_id=6080846508

def check_birthdays():
    while True:
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        birthdays_today = False
        try:
            with open('gimtadieniai.txt', 'r') as file:
                birthdays = file.readlines()
            if birthdays:
                for birthday in birthdays:
                    data = birthday.strip().split(',')
                    name = data[0].strip()
                    birth_date = data[1].strip()
                    if today[5:] == birth_date[5:]:
                        send_reminder(BirthdayReminder(name))
                        bot.send_message(chat_id, f"Šiandien yra {name} gimtadienis! Nepamiršk pasveikinti! 🎉")
                        birthdays_today = True
                if not birthdays_today:
                    bot.send_message(chat_id, "Šiandien gimtadienių nėra.")
        except FileNotFoundError:
            pass
        time.sleep(6000)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Parodyti gimtadieniu sąrašą', callback_data='show_list')
    btn2 = types.InlineKeyboardButton('Pridėti prie gimtadienių sąrašo', callback_data='add_to_list')
    btn3 = types.InlineKeyboardButton('Ištrinti iš gimtadienių sąrašo', callback_data='remove_from_list')
    markup.row(btn1)
    markup.row(btn2)
    markup.row(btn3)
    bot.send_message(message.chat.id, 'Labas', reply_markup=markup)
    check_birthdays()  

@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    if call.data == 'show_list':
        try:
            with open('gimtadieniai.txt', 'r') as file:
                birthdays = file.readlines()
            if birthdays:
                bot.send_message(call.message.chat.id, "Gimtadienių sąrašas:")
                for birthday in birthdays:
                    bot.send_message(call.message.chat.id, birthday.strip())
            else:
                bot.send_message(call.message.chat.id, 'Gimtadienių sąrašas yra tuščias.')
        except FileNotFoundError:
            bot.send_message(call.message.chat.id, 'Failas "gimtadieniai.txt" nerastas.')
    
    elif call.data == 'add_to_list':
        bot.send_message(call.message.chat.id, 'Įveskite vardą, pavardę ir gimimo datą.')
        bot.register_next_step_handler(call.message, handle_user_input)
    
    elif call.data == 'remove_from_list':
        bot.send_message(call.message.chat.id, 'Įveskite vardą, pavardę ir gimimo datą, kuriuos norite ištrinti.')
        bot.register_next_step_handler(call.message, handle_delete_input)

def handle_user_input(message):
    try:
        with open('gimtadieniai.txt', 'a') as file:
            file.write(message.text + '\n')
        bot.send_message(message.chat.id, 'Duomenys įrašyti sėkmingai į failą "gimtadieniai.txt"!')
    except Exception as e:
        bot.send_message(message.chat.id, f'Įvyko klaida įrašant duomenis: {e}')

def handle_delete_input(message):
    try:
        with open('gimtadieniai.txt', 'r') as file:
            lines = file.readlines()
        with open('gimtadieniai.txt', 'w') as file:
            for line in lines:
                if line.strip() != message.text.strip():
                    file.write(line)
        bot.send_message(message.chat.id, f'Duomenys su "{message.text.strip()}" ištrinti sėkmingai iš failo "gimtadieniai.txt"!')
    except Exception as e:
        bot.send_message(message.chat.id, f'Įvyko klaida trinant duomenis: {e}')

bot.polling(none_stop=True)
