import telebot
import json
import os
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

# Railway mein 'Variables' mein BOT_TOKEN naam ka variable banayein
BOT_TOKEN = os.environ.get("BOT_TOKEN") 
bot = telebot.TeleBot(BOT_TOKEN)

# Yahan apna GitHub Pages ka link dalein (https://username.github.io/telegram-store/)
WEB_APP_URL = "https://priyanshu-studio.github.io/telegram-store/"

@bot.message_handler(commands=['start'])
def start(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    # Store ka button
    web_app = WebAppInfo(url=WEB_APP_URL)
    markup.add(KeyboardButton("🛒 Mera Store Open Karein", web_app=web_app))
    bot.send_message(message.chat.id, "नमस्ते! हमारे स्टोर से खरीदारी करने के लिए नीचे दिए गए बटन पर क्लिक करें।", reply_markup=markup)

@bot.message_handler(content_types=['web_app_data'])
def handle_data(message):
    data = json.loads(message.web_app_data.data)
    bot.send_message(message.chat.id, f"✅ ऑर्डर प्राप्त हुआ!\n\n🛒 आइटम: {data['item']}\n💰 कीमत: ₹{data['price']}\n\nकृपया अपना डिलीवरी पता भेजें।")

print("Bot chal raha hai...")
bot.polling()
