import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart


bot = Bot(token="6878179107:AAF2iGai3fdWAJ6vLaZZcxAxaq-A7dHyPsY")

dp = Dispatcher()


@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Это была команда старт')


@dp.message()
async def echo(message: types.Message, bot: Bot):
    await bot.send_message(message.from_user.id, 'Ответ')
    await message.reply(message.text)
    await message.answer(message.text)
    # text = message.text
    # if text in ['Привет', 'привет', 'hi', 'Hello']:
    #     await message.answer('И тебе привет!')
    # elif text in ['Пока', 'пока', 'пакеда', 'До свидания']:
    #     await message.answer('И тебе пока!')
    # else:
    #     await message.answer(message.text)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


# Запуск бота
asyncio.run(main())