import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "")

API_ID = int(os.environ.get("API_ID", "28856445"))

API_HASH = os.environ.get("API_HASH", "25db48dbb9c6c44a7eb3761e877bf847")

STRING = os.environ.get("STRING", "")


bot = Client(

           "Rename",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
