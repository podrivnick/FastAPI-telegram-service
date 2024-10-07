import logging

from application.handlers.keyboard import (
    arts_handler,
    category_handler,
    choose_art_style_handler,
    choose_poem_author_handler,
    flower_handler,
    poems_handler,
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

    category_arts_message_handler = MessageHandler(filters.Text(["arts"]), arts_handler)
    get_random_flower_message_handler = MessageHandler(
        filters.Text(["flowers"]),
        flower_handler,
    )
    get_random_poem_message_handler = MessageHandler(
        filters.Text(["poems"]),
        poems_handler,
    )

    art_style_message_handler = MessageHandler(
        filters.Text(["Назад", "Baroque", "Romanticism", "Classicism", "Renaissance"]),
        choose_art_style_handler,
    )
    poem_style_message_handler = MessageHandler(
        filters.Text(["Назад", "А.С. Пушкин", "М.Ю. Лермонтов"]),
        choose_poem_author_handler,
    )

    application.add_handler(get_start_handler)
    application.add_handler(category_arts_message_handler)
    application.add_handler(get_random_flower_message_handler)
    application.add_handler(get_random_poem_message_handler)

    application.add_handler(art_style_message_handler)
    application.add_handler(poem_style_message_handler)

    return application


if __name__ == "__main__":
    start_app().run_polling()
