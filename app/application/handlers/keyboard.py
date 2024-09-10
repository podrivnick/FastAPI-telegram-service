from application.handlers.arts import get_random_art_handler
from telegram import (
    ReplyKeyboardMarkup,
    Update,
)
from telegram.ext import ContextTypes


async def category_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["flowers", "arts"],
    ]
    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        one_time_keyboard=True,
        resize_keyboard=True,
    )
    await update.message.reply_text(
        "Выберите категорию:",
        reply_markup=reply_markup,
    )


async def arts_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["Renaissance", "Romanticism"],
    ]
    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        one_time_keyboard=True,
        resize_keyboard=True,
    )

    await update.message.reply_text(
        "Выберите стиль искусства:",
        reply_markup=reply_markup,
    )


async def choose_art_style_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    art_direction = update.message.text.lower()
    await get_random_art_handler(update, context, art_direction)
