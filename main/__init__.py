#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = "24665357" #config("API_ID", default=None, cast=int)
API_HASH = "beb7e4b83ada668fa85f9a9b56338f1d" #config("API_HASH", default=None)
BOT_TOKEN = "6914999856:AAE7N7QocuVpQD_2FLhuomwTG5fOGAEAKHM" #config("BOT_TOKEN", default=None)
SESSION = "BQF4XQ0Aa8ge8YCvL7ql3OI1C8FTBwkGMhZx758fqeH-9IL9V3yuAC8JsjdLuAtWjpgWRIoT4RWop40HxYr4xKcFOYPMjW7TrrJKA5k2hZp-iiPmUlrQE1cIR0mCWsno7XuunB4Eb72E34zEIEqgjTSuahEB2Nyzu5-pmlM5ZXvNB4xHUjFus5nE8yENsly2assc_LXhmnyE5CF-prkwCEixGqVAL4jV_hiuQDBBKT1HsbPOlz7RlggSeACe_U7uMt_bjvWbuvgCD6beVhi3YRXBvklsGUiCaNuuw9mz0DLDsrqmUbHbViBm-xESJFFBtFsHhSGjMBf9cWJMkYWC7hwMIXmF-wAAAABmXyPCAA" #config("SESSION", default=None)
FORCESUB = "1002137417670" #config("FORCESUB", default=None)
AUTH = "1717511106" #config("AUTH", default=None, cast=int)

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
