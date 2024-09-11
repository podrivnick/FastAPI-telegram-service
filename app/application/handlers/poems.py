import re

from domain.poems.dto import GetPoemfromAPIResponses
from infrastructure.containers.factories import get_container
from infrastructure.services.base import BaseWebPoemsService
from telegram import Update
from telegram.ext import ContextTypes


async def get_random_poem_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    poem_author: str,
):
    container = get_container()

    async with container() as request_container:
        service = await request_container.get(BaseWebPoemsService)
        poem = await service.get_random_poem(poem_author)

        formatted_poem_text = format_poem(poem)

        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=formatted_poem_text,
            parse_mode="MarkdownV2",
        )


def escape_markdown_v2(text: str) -> str:
    return re.sub(r"([_.*`\[\]()~>#!\+-=|{}.!])", r"\\\1", text)


def format_poem(poem: GetPoemfromAPIResponses) -> str:
    escaped_title = escape_markdown_v2(poem.poem_title)
    escaped_author = escape_markdown_v2(poem.poem_author)
    escaped_text = escape_markdown_v2(poem.poem_text)
    escaped_date = escape_markdown_v2(poem.poem_date)

    formatted_poem = (
        f"{escaped_author}\n\n"
        f"*{escaped_title}\n\n*"
        f"{escaped_text}\n\n"
        f"*Дата:* {escaped_date}"
    )

    return formatted_poem
