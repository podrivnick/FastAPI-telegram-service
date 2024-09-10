from application.handlers.arts import get_random_art_handler
from application.handlers.start import start_handler
from settings.config import get_config
from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Update,
)
from telegram.ext import (
    ApplicationBuilder,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
)


async def category_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "arts":
        await arts_handler(update, context)


async def arts_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("Renaissance", callback_data="renaissance"),
            InlineKeyboardButton("Romanticism", callback_data="romanticism"),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Выберите стиль искусства:",
        reply_markup=reply_markup,
    )


async def choose_art_style_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    art_style = query.data
    await get_random_art_handler(update, context, art_style)


def start_app() -> ApplicationBuilder:
    config = get_config()

    application = ApplicationBuilder().token(config.TG_TOKEN).build()

    get_start_handler = CommandHandler("start", start_handler)

    application.add_handler(get_start_handler)
    application.add_handler(CallbackQueryHandler(category_handler))
    application.add_handler(
        CallbackQueryHandler(
            choose_art_style_handler,
            pattern="^(renaissance|romanticism)$",
        ),
    )

    return application


if __name__ == "__main__":
    start_app().run_polling()
