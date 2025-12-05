from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, WebAppInfo
from telegram.ext import ContextTypes

from db import add_user


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    added = add_user(
        tg_id=update.message.from_user.id,
        full_name=update.message.from_user.full_name,
        username=update.message.from_user.username
    )

    await update.message.reply_text(
        text=f"""Assalomu Alaykum, {update.message.from_user.first_name}!

Ijodimizga qiziqish bildirganingiz uchun tashakkur!

Hozircha siz uchun futbolka, xudi, svitshot, kepka va stikerlar mavjud...""",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(
                        text='🔥 Mahsulotlar',
                        web_app=WebAppInfo(url='https://uzum.uz')
                    ),
                    KeyboardButton(text='📥Savat'),
                ],
                [
                    KeyboardButton(text='💼 Hamkorlik'),
                    KeyboardButton(text='ℹ️ Ma\'lumot')
                ],
                [KeyboardButton(text='🌐 Tilni tanlash')]
            ],
            resize_keyboard=True,
        )
    )


async def main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        text=f"""Assalomu Alaykum, {update.message.from_user.first_name}!""",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(
                        text='🔥 Mahsulotlar',
                        web_app=WebAppInfo(url='https://uzum.uz')
                    ),
                    KeyboardButton(text='📥Savat'),
                ],
                [
                    KeyboardButton(text='💼 Hamkorlik'),
                    KeyboardButton(text='ℹ️ Ma\'lumot'),
                ],
                [KeyboardButton(text='🌐 Tilni tanlash')]
            ],
            resize_keyboard=True,
        )
    )


async def order(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["state"] = "order"
    await update.message.reply_text("Sizning savatingiz bo'sh")


async def about_us(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["state"] = "about_us"
    await update.message.reply_text(
        text="""Biz sizning kompaniyangiz bilan hamkorlik qilishdan mamnunmiz..."""
    )


async def show_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["state"] = "show_info"
    await update.message.reply_text(
        text="Kerakli bo'limni tanlang ⬇️",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text='✍️ Izoh qoldirish')],
                [
                    KeyboardButton(text='🚀 Yetkazib berish shartlari'),
                    KeyboardButton(text='☎️ Kontaktlar'),
                ],
                [KeyboardButton(text='🏠 Bosh menyu')],
            ],
            resize_keyboard=True,
        )
    )


async def comment(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["state"] = "comment"
    await update.message.reply_text(
        text="""5 ballik tizim asosida baholang""",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton('😊Menga hamma narsa yoqdi, 5 ❤️')],
                [KeyboardButton('☺️Yaxshi, 4 ⭐️⭐️⭐️⭐️')],
                [KeyboardButton('😐Qo\'niqarli, 3⭐️⭐️⭐️')],
                [KeyboardButton('☹️Yoqmadi, 2 ⭐️⭐️')],
                [KeyboardButton('😤Men shikoyat qilmoqchiman 👎🏻')],
                [KeyboardButton('🏠 Bosh menyu')],
            ],
            resize_keyboard=True
        )
    )


async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Teskari aloqa uchun: @tirik_chilik")


async def sent_order(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """Yetkazib berish shartlari:
1–3 ish kuni..."""
    )


async def like_bot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["state"] = "like_bot"
    await update.message.reply_text(
        text="Mamnun qolganingizdan xursandmiz 😊",
        reply_markup=ReplyKeyboardMarkup([[KeyboardButton("⬅️ Orqaga")]], resize_keyboard=True)
    )


async def good_bot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["state"] = "good_bot"
    await update.message.reply_text(
        text="Maslahatlaringiz bormi? 😊",
        reply_markup=ReplyKeyboardMarkup([[KeyboardButton("⬅️ Orqaga")]], resize_keyboard=True)
    )


async def satisfactory_bot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["state"] = "satisfactory_bot"
    await update.message.reply_text(
        text="Takliflaringizni yozing 🙂",
        reply_markup=ReplyKeyboardMarkup([[KeyboardButton("⬅️ Orqaga")]], resize_keyboard=True)
    )


async def not_like_bot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["state"] = "not_like_bot"
    await update.message.reply_text(
        text="Takliflaringiz bormi?",
        reply_markup=ReplyKeyboardMarkup([[KeyboardButton("⬅️ Orqaga")]], resize_keyboard=True)
    )


async def complaint_bot(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["state"] = "complaint_bot"
    await update.message.reply_text(
        text="Shikoyatingizni yozing",
        reply_markup=ReplyKeyboardMarkup([[KeyboardButton("⬅️ Orqaga")]], resize_keyboard=True)
    )


async def back(update: Update, context: ContextTypes.DEFAULT_TYPE):
    current = context.user_data.get("state")

    if current in ("order", "about_us", "comment"):
        await main_menu(update, context)
    else:
        await comment(update, context)
