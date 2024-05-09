from aiogram.types import (
    KeyboardButton,
    ReplyKeyboardMarkup,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🌏 Shaharlar ro'yxati", callback_data=f"city")]
    ]
)

viloyat = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✨ Andijon", callback_data="tur-андижан"),
            InlineKeyboardButton(text="✨ Buxoro", callback_data="tur-бухара"),
        ],
        [
            InlineKeyboardButton(text="✨ Farg'ona", callback_data="tur-фергана"),
            InlineKeyboardButton(text="✨ Jizzax", callback_data="tur-джизак"),
        ],
        [
            InlineKeyboardButton(text="✨ Namangan", callback_data="tur-наманган"),
            InlineKeyboardButton(text="✨ Navoiy", callback_data="tur-навои"),
        ],
        [
            InlineKeyboardButton(text="✨ Qarshi", callback_data="tur-карши"),
            InlineKeyboardButton(text="✨ Nukus", callback_data="tur-нукус"),
        ],
        [
            InlineKeyboardButton(text="✨ Samarqand", callback_data="tur-самарканд"),
            InlineKeyboardButton(text="✨ Sirdaryo", callback_data="tur-сырдарья"),
        ],
        [
            InlineKeyboardButton(text="✨ Tezmiz", callback_data="tur-термез"),
            InlineKeyboardButton(text="✨ Toshkent", callback_data="tur-ташкент"),
        ],
        [
            InlineKeyboardButton(text="✨ Urganch", callback_data="tur-ургенч"),
            InlineKeyboardButton(text="◀️ Orqaga", callback_data="back"),
            
        ],
    ]
)

def turi(item):
    btn = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🗓 Bugungi", callback_data=f"info-kun-{item}"),
                InlineKeyboardButton(text="📆 Haftalik", callback_data=f"info-hafta-{item}"),
            ],
            [
                InlineKeyboardButton(text="◀️ Orqaga", callback_data="city")
            ]
        ]
    )
    
    return btn
