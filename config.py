from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from bs4 import BeautifulSoup as X
import requests
from googletrans import Translator

tr = Translator()

TOKEN = '7002675047:AAG5p7chNHV7KGR_xwXmXwWCgE1arXNSNh8'

channel = "WebKoderUz_Baza"
admin = "5668945618"
bot_user = "visualcoderbot"
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
