from infrastructure.containers.factories import get_container
from infrastructure.services.base import BaseWebFlowersService
from telegram import Update
from telegram.ext import ContextTypes


async def get_random_flower_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    container = get_container()

    async with container() as request_container:
        service = await request_container.get(BaseWebFlowersService)
        flower = await service.get_random_flower()

        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=flower.flower_name,
            parse_mode="MarkdownV2",
        )

        await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=open(flower.flower_path, "rb"),
            caption=flower.flower_name,
            parse_mode="MarkdownV2",
        )
