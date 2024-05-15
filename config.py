from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from bs4 import BeautifulSoup as X
import requests
from googletrans import Translator

tr = Translator()

TOKEN = '7162331887:AAFW5qxhaF6M-Z2LyfPU6fGWzEY153JFfTk'

channel = "WebKoderUz_Baza"
admin = "5668945618"
bot_user = "visualcoderbot"
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
