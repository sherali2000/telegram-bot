import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, FSInputFile
from aiogram.filters import Command

TOKEN = "8294441580:AAHFWKcjJLiTco6Fiw3VQV7u7ERdg2SiRYk"
VOTE_LINK = "https://openbudget.uz/boards/initiatives/initiative/53/0c5d0c49-d3d7-4848-94e4-1bcfe7d65059"

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start_command(message: types.Message):

    await message.answer(
        "Assalomu alaykum! Loyihaga ovoz berish uchun quyidagi ko‘rsatmalarni kuzatib boring:"
    )

    photo1 = FSInputFile("step1.jpg")
    await message.answer_photo(
        photo=photo1,
        caption="1-qadam: SMS orqali tugmasini bosing."
    )

    photo2 = FSInputFile("step2.jpg")
    await message.answer_photo(
        photo=photo2,
        caption="2-qadam: Rasmda ko'rsatilgandek telefon raqam yozasiz va A rasmdagi hariflarni B rasmda topasiz. Keyin SMS kodni yuborish tugmasini bosing."
    )

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🗳 Ovoz berish",
                    url=VOTE_LINK
                )
            ]
        ]
    )

    await message.answer(
        "Ovoz berish uchun tugmani bosing:",
        reply_markup=keyboard
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())