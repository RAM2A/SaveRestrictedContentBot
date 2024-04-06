#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = "22988891" #config("API_ID", default=None, cast=int)
API_HASH = "c4a15361a9f8f6fc8d628cf8d62ebd5b" #config("API_HASH", default=None)
BOT_TOKEN = "7000214557:AAH68Yi1sh63mzrXvaMCvy8CzZuPwgDWOwQ" #config("BOT_TOKEN", default=None)
SESSION = "BQFeyFsAvLn8SOVL1gVE1Y5eIm2pgdvTdAvMM64Dqbr2N3i5mz7AhYzSkGp4ltfyzwJWTGhg3CRwURBJXvWZ5bQcJ9qn7xFhDcvSSsv-Rs5rIqha6uBYPlU2eC1ALCodugU1_qMPgmzQMEa33rHA9UhlPYwkep1GRxpPh7r0B63iOBiJdgf2hpmkIMrcR2fxaSsoLyfp-q0zMbVRuC4gwyAOdjO-5MxDE47HAqGEmJYqe2L_IRfKnEvUQ0Kj2fiZHWHcKq7MV7oZWQkDyVT-o-qv0XG_hEE6PwwGplgEL4kXMP8z5UWM6HhrHs3MvqYx85SJnwrPQ1DQ4AtbGUXSxx9xJv2BfAAAAABpIr7bAA" #config("SESSION", default=None)
FORCESUB = "1002136298814" #config("FORCESUB", default=None)
AUTH = "1763884763" #config("AUTH", default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
