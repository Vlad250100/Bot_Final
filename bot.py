import telebot 
import random

token = "1043599060:AAFNgKZFLs3i8LnBX8YYeMvvQmB4ObSk0Cg"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['cat']) 
def send_cat(message): 
    cat_number = str(random.randint(1,3))
    cat_img = open('Котики/' + cat_number + '.jpg', 'rb')
    bot.send_photo(message.chat.id, cat_img)

@bot.message_handler(commands=['dog']) 
def send_dog(message): 
    dog_number = str(random.randint(1,3))
    dog_img = open('Песики/' + dog_number + '.jpg', 'rb')
    bot.send_photo(message.chat.id, dog_img)
  
  
bot.polling()
