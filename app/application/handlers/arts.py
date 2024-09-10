from infrastructure.containers.factories import get_container
from infrastructure.services.base import BaseWebArtsService
from telegram import Update
from telegram.ext import ContextTypes


async def get_random_art_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
    art_direction: str,
):
    container = get_container()

    async with container() as request_container:
        service = await request_container.get(BaseWebArtsService)
        art = await service.get_random_art(art_direction)

        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=art.art_description,
            parse_mode="MarkdownV2",
        )

        await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=open(art.art, "rb"),
            caption=art.art_name,
            parse_mode="MarkdownV2",
        )
