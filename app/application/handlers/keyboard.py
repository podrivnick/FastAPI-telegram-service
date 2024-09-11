from application.handlers.arts import get_random_art_handler
from application.handlers.flowers import get_random_flower_handler
from application.handlers.poems import get_random_poem_handler
from telegram import (
    ReplyKeyboardMarkup,
    Update,
)
from telegram.ext import ContextTypes


async def category_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["flowers", "arts", "poems"],
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


async def flower_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await get_random_flower_handler(update, context)


async def arts_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["Renaissance", "Romanticism"],
        ["Назад"],
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
    command = update.message.text.lower()
    if command == "назад":
        await category_handler(update, context)
    else:
        await get_random_art_handler(update, context, command)


async def poems_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["А.С. Пушкин", "М.Ю. Лермонтов"],
        ["Назад"],
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


async def choose_poem_author_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    command = update.message.text
    if command == "назад":
        await category_handler(update, context)
    else:
        await get_random_poem_handler(update, context, command)
