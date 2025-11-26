import os
import logging
from telegram.ext import Application, CommandHandler

# Безопасное получение переменных окружения
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8291131417:AAGc9GBjuy_m3ulbE6LurWchMmIVoHsa5w4")
ADMIN_ID = os.environ.get("ADMIN_ID", "123456789")  # Замените на ваш ID

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update, context):
    await update.message.reply_text("🎵 Студия звукозаписи! Бот работает 24/7!")

async def book(update, context):
    await update.message.reply_text("📞 Для записи: @studiosomisics_admin")

def main():
    if not BOT_TOKEN:
        logger.error("BOT_TOKEN не установлен!")
        return
        
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("book", book))
    
    print("Бот запущен...")
    application.run_polling()

if __name__ == "__main__":
    main()
