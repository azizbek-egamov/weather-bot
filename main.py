# START CODING

from functions import *


@dp.message(CommandStart())
async def start_comand(message: Message):
    await message.answer(
        f"💥 Assalomu alaykum {message.from_user.full_name}\n\n⚡️ Bu bot orqali ob-havo ma'lumotlarini olishingiz mumkin.",
        reply_markup=menu,
    )


@dp.callback_query(F.data == "city")
async def viloyats(callback: CallbackQuery):
    await bot.delete_message(callback.message.chat.id, callback.message.message_id)
    await callback.message.answer(
        "💥 Marhamat, o'zingizga kerakli shaharni tanlang:", reply_markup=viloyat
    )


@dp.callback_query(F.data.startswith("tur-"))
async def turr(callback: CallbackQuery):
    await bot.delete_message(callback.message.chat.id, callback.message.message_id)
    tur = callback.data.split("-")[1]
    await callback.message.answer(
        "🪙 Qaysi kunni bilmoqchisiz: ", reply_markup=turi(tur)
    )


@dp.callback_query(F.data.startswith("info-"))
async def inf(callback: CallbackQuery):
    action = callback.data.split("-")
    a = action[1]
    b = action[2]

    await bot.delete_message(callback.message.chat.id, callback.message.message_id)

    ie = await callback.message.answer(
        "Ilitmos kutib turing, ma'lumotlarni yuklayabman"
    )

    bt = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="◀️ Orqaga", callback_data=f"tur-{b}")]
        ]
    )

    if a == "kun":
        url = requests.get(f"https://sinoptik.ua/погода-{b}")
        html_t = X(url.content, "html.parser")
        a = html_t.select("#content")
        l = list()
        r = list()
        for i in a:
            for j in range(1):
                l.append(
                    [
                        tr.translate(i.select(".date")[j].text, dest="uz").text,
                        tr.translate(i.select(".month")[j].text, dest="uz").text,
                        tr.translate(i.select(".max")[j].text, dest="uz").text,
                        tr.translate(i.select(".min")[j].text, dest="uz").text,
                    ]
                )

        for i in html_t.select(".tabsContent"):
            for j in range(1):
                r.append(
                    [
                        tr.translate(i.select(".description")[j].text, dest="uz").text,
                        tr.translate(i.select(".today-time")[j].text, dest="uz").text,
                        tr.translate(i.select(".infoDaylight")[j].text, dest="uz").text,
                    ]
                )
        times = re.findall(r"\b\d{2}:\d{2}\b", r[0][2])
        await bot.delete_message(callback.message.chat.id, ie.message_id)
        await callback.message.answer(
            f"""<i>ℹ️ {r[0][1]}:
                                      
✨ Bugun: {int(l[0][0])} - {l[0][1]}
⚡️ Harorat: min {str(l[0][3]).split()[1]} - {l[0][2]}

💥 {r[0][0]}
🌤 Quyosh chiqishi: {times[0]}
🌥 Quyosh botishi: {times[1]}</i>""",
            reply_markup=bt,
        )
    elif a == "hafta":
        url = requests.get(f"https://sinoptik.ua/погода-{b}")
        html_t = X(url.content, "html.parser")
        a = html_t.select("#content")
        l = list()
        for i in a:
            for j in range(7):
                l.append(
                    [
                        tr.translate(i.select(".date")[j].text, dest="uz").text,
                        tr.translate(i.select(".month")[j].text, dest="uz").text,
                        tr.translate(i.select(".max")[j].text, dest="uz").text,
                        tr.translate(i.select(".min")[j].text, dest="uz").text,
                    ]
                )
        await bot.delete_message(callback.message.chat.id, ie.message_id)
        t = ""
        y = 0
        for i in l:
            t += f"""✨ Sana: {int(l[y][0])} - {l[y][1]}
⚡️ Harorat: min {str(l[y][3]).split()[1]} - {l[y][2]}\n\n"""
            y += 1
        await callback.message.answer(
            f"""Haftalik ob xavo ma'lumotlari
                                      
{t}""",
            reply_markup=bt,
        )


# html_t = X(url.content, "html.parser")
# a = html_t.select("#content")
# l = list()
# for i in a:
#     for j in range(1):
#         l.append([tr.translate(i.select('.date')[j].text, dest="uz").text, tr.translate(i.select('.month')[j].text, dest="uz").text, tr.translate(i.select('.max')[j].text, dest="uz").text, tr.translate(i.select('.min')[j].text, dest="en").text])


async def main() -> None:
    dp.message.middleware.register(ThrottlingMiddleware())
    dp.update.middleware.register(joinchat())
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(main())
    except:
        print("Jarayon yakunlandi")
