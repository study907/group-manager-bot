import telebot
import os

API_TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(content_types=['new_chat_members'])
def welcome(message):
    for user in message.new_chat_members:
        bot.send_message(message.chat.id, f"👋 स्वागत है {user.first_name} जी!")

@bot.message_handler(func=lambda msg: msg.text and msg.text.lower() in ['hi','hello','namaste'])
def greet(message):
    bot.reply_to(message, "🙏 नमस्ते! कैसे मदद कर सकता हूँ?")

@bot.message_handler(commands=['rules'])
def rules(message):
    bot.reply_to(message, "📜 *Group Rules:*\n1. Spam मना है\n2. सभी से विनम्र रहें\n3. Admin के निर्देश मानें", parse_mode='Markdown')

@bot.message_handler(func=lambda msg: msg.text)
def filter_spam(message):
    spam = ['spam','subscribe','promo']
    if any(w in message.text.lower() for w in spam):
        try:
            bot.delete_message(message.chat.id, message.message_id)
        except:
            pass

bot.polling()
