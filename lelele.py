import telebot
import os
bot = telebot.TeleBot("7419030779:AAE728r81Os2LVrQGfyzJTlmtCVVOaAdnNg")

images = os.listdir('images')

@bot.message_handler(commands=['start'])
def send_start(message):
    bot.send_message(message.chat.id, '''
    Привет! Я могу помочь тебе с экологией! Напиши /more чтобы узнать,
как правильно утилизировать мусор.
                     ''')
    
@bot.message_handler(commands=['more'])
def send_util(message):
    bot.send_message(message.chat.id, '''
    Итак, утилизация мусора - важный процесс, 
который помогает сократить загрязнение и уменьшить нагрузку на полигоны. 
Основные шаги включают разделение отходов на категории: органические (пищевые остатки), 
пластик, бумага и картон, стекло, металл и опасные (батарейки, электроника). 
Важно использовать специальные контейнеры для разных типов отходов, 
а для органических отходов можно применять компостирование. 
Сокращение мусора также играет значительную роль: стоит отказаться от одноразовых предметов, 
стремиться к минимизации упаковки и ремонтировать вещи. 
Обращай внимание на безопасную утилизацию опасных отходов через специализированные пункты. 
Напиши /crafts чтобы узнать, какие поделки можно сделать из мусора.
                     ''')
    
@bot.message_handler(commands=['crafts'])
def send_crafts1(message):
    with open(f'images/img1.jpg', 'rb') as f:  
        bot.send_photo(message.chat.id, f) 

    with open(f'images/img2.jpg', 'rb') as f:  
        bot.send_photo(message.chat.id, f) 

    with open(f'images/img3.jpg', 'rb') as f:  
        bot.send_photo(message.chat.id, f) 

bot.polling()
