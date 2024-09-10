from app.settings.config import get_config
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
)


def start_app() -> ApplicationBuilder:
    config = get_config()
    application = ApplicationBuilder().token(config.TG_TOKEN).build()
    StartBotHandler = "sd"
    start_handler = CommandHandler("start", StartBotHandler)

    application.add_handler(start_handler)

    return application


if __name__ == "__main__":
    start_app().run_polling()
