from app.settings.config import get_config
from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Update,
)
from telegram.ext import ContextTypes


async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    config = get_config()

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=config.GREETING_TEXT,
    )

    keyboard = [
        [
            InlineKeyboardButton("Flowers", callback_data="flowers"),
            InlineKeyboardButton("Arts", callback_data="arts"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Выберите категорию:",
        reply_markup=reply_markup,
    )
