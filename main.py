import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
import asyncio
from aiogram import Bot, Dispatcher, executor
import csv, datetime, pymysql

API_TOKEN = "5608313623:AAForTlSQjvPcbIGtSY1Twuf4NgWA0S9XE8"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    await message.reply("Привет!")
    statistics(message.chat.id, message.text, message.from_user.username)
    stat(message.chat.id, message.text)

def stat(user_id, command):
    connection = pymysql.connect("sql.freedb.tech", "freedb_KryaMaybe", "T6cksyH8%NrgH4Y", "freedb_KryaMaybe")
    cursor = connection.cursor()
    data = datetime.datetime.today().strftime("%d-%m-%Y %H:%M")
    cursor.execute("INSERT INTO stat (user_id, user_command, date) VALUES ('%s', '%s', '%s', '%s')" % (user_id, command, data))
    connection.commit()
    cursor.close()
    with open("data.csv","a", newline="") as fil:
        wr = csv.writer(fil, delimiter=";")
        wr.writerow([data, user_id, command])

if __name__ == "__main__":
    executor.start_polling(dp)
