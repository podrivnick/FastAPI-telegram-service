from application.handlers.utils import escape_markdown_v2
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
        art_photo = await service.get_art_photo_from_remote_storage(
            "galeryshuffle",
            art.art,
        )

        formated_art_description = escape_markdown_v2(art.art_description)
        formated_art_title = escape_markdown_v2(art.art_name)

        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=formated_art_description,
            parse_mode="MarkdownV2",
        )

        await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=art_photo,
            caption=formated_art_title,
            parse_mode="MarkdownV2",
        )
