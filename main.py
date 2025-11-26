import os
import logging
import sqlite3
from datetime import datetime, timedelta
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, ConversationHandler

# Настройка
BOT_TOKEN = os.environ["BOT_TOKEN"]
ADMIN_ID = int(os.environ.get("ADMIN_ID", "123456789"))

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    welcome_text = f"""
Привет, {user.first_name}! 🎵
Добро пожаловать в студию звукозаписи!

Команды:
/book - Записаться в студию
/mybookings - Мои записи
/cancel - Отмена

Бот работает 24/7! ⚡
    """
    await update.message.reply_text(welcome_text)

# Команда /book
async def book(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📞 Для записи в студию свяжитесь с администратором: @studiosomisics_admin\n\n"
        "Или оставьте заявку:\n"
        "1. Ваше имя\n"
        "2. Телефон\n"
        "3. Желаемая дата и время\n"
        "4. Услуга"
    )

# Команда /mybookings
async def my_bookings(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Функция просмотра записей скоро будет доступна!")

# Обработчик ошибок
async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.error(f"Ошибка: {context.error}")

def main():
    # Создание приложения
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Добавление обработчиков
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("book", book))
    application.add_handler(CommandHandler("mybookings", my_bookings))
    application.add_error_handler(error_handler)
    
    # Запуск бота
    print("Бот запущен...")
    application.run_polling()

if __name__ == "__main__":
    main()
