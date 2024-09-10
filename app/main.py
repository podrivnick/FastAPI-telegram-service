import logging

from application.handlers.keyboard import (
    arts_handler,
    category_handler,
    choose_art_style_handler,
)
from settings.config import get_config
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    filters,
    MessageHandler,
)


async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    config = get_config()

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=config.GREETING_TEXT,
    )
    await category_handler(update, context)


def start_app() -> ApplicationBuilder:
    config = get_config()

    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

    application = ApplicationBuilder().token(config.TG_TOKEN).build()

    get_start_handler = CommandHandler("start", start_handler)
    category_message_handler = MessageHandler(filters.Text(["arts"]), arts_handler)
    art_style_message_handler = MessageHandler(
        filters.Text(["Renaissance", "Romanticism"]),
        choose_art_style_handler,
    )

    application.add_handler(get_start_handler)
    application.add_handler(category_message_handler)
    application.add_handler(art_style_message_handler)

    return application


if __name__ == "__main__":
    start_app().run_polling()
