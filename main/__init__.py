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
BOT_TOKEN = "6700540841:AAEzEG75XEQXqfTGmIvy136zVclAUBxQKOI" #config("BOT_TOKEN", default=None)
SESSION = "BQF4XQ0AtHNaResIjhYD_3CnwMALlYGhTeU1eyaWJwS8p1K4lRfqu6Pe5v2DX7r60cOZmDCgvWoN1g5DfN-XI_ynsPmqUXiM3HesFihFUYB5WcMv4ZgeAGtBmvmuQ9Nlpm-yKlamynvty-ym5aLBgYhCoHf-r08btcrh3OpiB68pehGIO_A4sCZUuIwulkXalkMfKARwRzTeB8EqtDri_9n7GzD6ntcDvM6ozzyQhtAaJqGETSFvHXlJmsmtvKAHIUQwQmUOSB7Xvp1qctdtvw9Se_6cPiOqfcXquz164zB8dUoRpuUaK-LhnpKMSaVGTiLw24-6A4zXKf6TUot8ZCyBBGQUGAAAAABmXyPCAA" #config("SESSION", default=None)
FORCESUB = "2137417670" #config("FORCESUB", default=None)
AUTH = "1717511106" #config("AUTH", default=None)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
  

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
