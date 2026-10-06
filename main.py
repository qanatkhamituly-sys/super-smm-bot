import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

# ТОКЕНДІ ОСЫ ЖЕРГЕ ЖАЗАСЫҢ
BOT_TOKEN = "123456:ABC-ТОКЕНІҢ_ОСЫНДА"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(msg: types.Message):
    text = f"""
Сәлем {msg.from_user.first_name}! 👋

Мен Super SMM Botпын 🤖
Ақтөбеден сәлем!

/start - басы
"""
    await msg.answer(text)

@dp.message()
async def echo(msg: types.Message):
    await msg.answer("Хабарлама алдым! Маған @qanat_khamituly жаз")

async def main():
    print("Бот іске қосылды!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
