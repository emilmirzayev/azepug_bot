# coding: utf8


import time
import telebot
import requests
# from bs4 import BeautifulSoup



bot = telebot.TeleBot(token="")

commands = {  # command description used in the "help" command
              'start': 'Salamlama',
              'help': 'Mövcud əmrləri göstər',
              'kitab': 'Faydalı kitablar',
              'admin': 'Adminlə əlaqə',
              "video": "Faydalı videodərs pleylistləri"
}


def findat(msg):
    # from a list of texts, it finds the one with the '@' sign
    for i in msg:
        if '@' in i:
            return i

# def check_if_active(url):
#     page = requests.get(url)
#     soup = BeautifulSoup(page.text, 'html.parser')

#     if 'Page Not Found' in soup.title.text:
#         # soup.title.text gives the text of the <title> tag
#         return False
#     else:
#         return True

@bot.message_handler(commands=['start']) # welcome message handler
def send_welcome(message):
    bot.reply_to(message, """Salam, Azərbaycan Python istifadəçiləri qrupuna xoş gəlmisiniz. Mümkün əmr siyahısını görmək üçün /help yazın. Bizi fesbukda da izləyə bilərsiniz.\n
                            https://www.facebook.com/groups/python.az""")

@bot.message_handler(commands=['help'])
def command_help(message):
    # cid = m.chat.id
    help_text = "Aşağıdakı kömək komandaları mövcuddur \n"
    for key in commands:  # generate help text out of the commands dictionary defined at the top
        help_text += "/" + key + ": "
        help_text += commands[key] + "\n"
    bot.reply_to(message, help_text) # send the generated help page

@bot.message_handler(commands = ["admin"])
def tag_admin(message):
    bot.reply_to(message, "Qrup admini: @emilmirza \nƏgər python ilə bağlı sualınız varsa, qrupa birbaşa yaza bilərsiniz. Nəzərə alın ki, sual qısa və aydın olmaqla yanaşı, həm də suala cavab üçün yeni suallar doğurmayacaq qədər dolğun olmalıdır.")


@bot.message_handler(commands = ["kitab"])
def book_suggestion(message):
    bot.reply_to(message, "Python öyrənmək üçün top 5 kitab:\n 1: Python Crash Course (https://nostarch.com/pythoncrashcourse) \n 2: Learn Python 3 the Hard Way (https://learnpythonthehardway.org/python3/) \n 3: Fluent Python: Clear, Concise, and Effective Programming (http://shop.oreilly.com/product/0636920032519.do) \n 4: Think Python: How to Think Like a Computer Scientist, 2nd edition (https://greenteapress.com/wp/think-python-2e/) \n 5: Rəsmi Python öyrədici materialları (https://docs.python.org/3/tutorial/index.html)")



@bot.message_handler(commands = ["video"])
def video_suggestion(message):
    bot.reply_to(message, "Python öyrənmək üçün YouTube pleylistlər")



@bot.message_handler(func=lambda message: True, content_types=['text'])
def command_default(message):
    # this is the standard reply to a normal message
    bot.reply_to(message, "İnsan olmadığımçün, insan dilini elə də yaxşı anlamıram \nBəlkə kömək əmrini istifadə edəsiniz? /help")



while True:
    try:
        bot.polling(none_stop=True)
        # ConnectionError and ReadTimeout because of possible timout of the requests library
        # maybe there are others, therefore Exception
    except Exception:
        time.sleep(15)

