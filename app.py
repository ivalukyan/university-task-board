import asyncio
import logging

from aiogram import Bot, Dispatcher, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

from config import TELEGRAM_TOKEN

router = Router()
bot = Bot(token=TELEGRAM_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))


@router.message(CommandStart())
async def command_start(message: Message) -> None:
    await message.answer(text=f"Здравствуйте, {message.from_user.first_name}")


async def main():
    """
    bot - main construction fun of bot
    dp - dispatcher
    """
    # Initialize Bot instance with default bot properties which will be passed to all API calls

    dp = Dispatcher()
    dp.include_routers(router)

    # Start event dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    asyncio.run(main())
