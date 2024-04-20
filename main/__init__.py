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
SESSION = "BQF4XQ0AYNVos0LGcO6kXmYonSvo6KV8t1DC2HZtOhnytz_gHjkbsKguLjqlkdP9ev3PSYPf1N_H-vTM9p53tHT66bRPYveM2cYGdg_zbW8Z38NxxrNNoC_7npVbGqzUT3nuN5rtSdG5Ise_nD6UXiYdheiKEanKKY5BeX9LBzjGNzA_OjNhDumIKPAVgf96TIDBJLnSLSQsCEWWU3S7MR8PrVP1d1-Awiz-2KPb3xlwRLdHiwmhi6NpKVnoCsFsF04KwyBfCvZkRO3jv1h804FsksWPVSaiNBdHlVybaB5PjLwnqPKGUbXxI_GLB9URVIO9g7zYkVeNJPJKurpCK6npvFSOHgAAAAGPYiOpAQ" #config("SESSION", default=None)
FORCESUB = "2137417670" #config("FORCESUB", default=None)
AUTH = "1717511106" #config("AUTH", default=None)

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
