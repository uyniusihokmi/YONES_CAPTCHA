
import requests
import telebot
from io import BytesIO

bot = telebot.TeleBot("7920653493:AAF3E_fnCWCdF210ZYVv_cgpFBz6YIvvTik")

@bot.message_handler(func=lambda message: message.text.startswith("http"))
def handle_captcha_link(message):
    url = message.text.strip()
    try:
        response = requests.get(url)
        if response.status_code == 200 and "image" in response.headers.get("Content-Type", ""):
            img_data = BytesIO(response.content)
            img_data.name = "captcha.png"
            bot.send_photo(chat_id=6394651560, photo=img_data)
        else:
            bot.reply_to(message, "لینک معتبر عکس نبود یا دانلود نشد.")
    except Exception as e:
        bot.reply_to(message, f"خطا در دانلود تصویر: {str(e)}")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام! لینک عکس کپچا رو بفرست، من برات فوراً دانلود و ارسال می‌کنم.")

print("ربات فعال است...")
bot.infinity_polling()
