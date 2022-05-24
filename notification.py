import asyncio
import aioschedule
from aiogram import types, Dispatcher
from config import bot


async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = message.from_user.id
    await bot.send_message(chat_id=message.chat.id, text="Got your id")

async def reminder():
        await bot.send_message(chat_id=message.chat.id, text="О чем напомнить?f'\nДля выхода отправьте \'exit\n")

 async def display_date():
        loop = asyncio.get_running_loop()
        end_time = loop.time() + 5.0
            while True:
                print(datetime.datetime.now())
                if (loop.time() + 1.0) >= end_time:
                    break
                await asyncio.sleep(1)

        asyncio.run(display_date())

# async def go_to_sleep():
#     await bot.send_message(chat_id=chat_id, text="Пора спать!")


#async def wake_up():
    video = open("media/erjan.mp4", "rb")
    print(video)
    #await bot.send_video(chat_id=chat_id, video=video, caption="Вставай")


#async def scheduler():
    # aioschedule.every().day.at("19:44").do(go_to_sleep)
    aioschedule.every().day.at("20:04").do(wake_up)

    #while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)


def register_handler_notification(dp: Dispatcher):
    dp.register_message_handler(get_chat_id, lambda word: 'разбуди' in word.text)


