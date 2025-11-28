from telegram.ext import CallbackContext
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType, WebAppInfo

from db import add_user


def start(update: Update, context: CallbackContext):
    if add_user(
        tg_id=update.message.from_user.id,
        full_name=update.message.from_user.full_name,
        username=update.message.from_user.username
    ):
        update.message.reply_text(
            text=f"""Assalomu Alaykum, {update.message.from_user.first_name}!

Ijodimizga qiziqish bildirganingiz uchun tashakkur!

Hozircha siz uchun futbolka, xudi, svitshot, kepka va stikerlar mavjud. Yaqin orada tanlovni kengaytiramiz. Aytganday, istagan turdagi kiyim buyurtma berganlarlarga qo'shimcha ravishda stikerpak sovg'a qilinadi :)

Toshkent bo‘yicha yetkazib berish: 1–3 ish kuni
O‘zbekiston bo‘yicha yetkazib berish: 3–7 ish kuni
O‘zbekiston bo‘yicha jo‘natmalar seshanba va juma kunlari amalga oshiriladi

450 000 so'mdan ortiq buyurtmalarni yetkazib berish - tekin!

Agar bu shartlar sizni qoniqtirsa, “🔥 Mahsulotlar” bo'limiga o'tish orqali buyurtma berishni boshlashingiz mumkin.""",
            reply_markup=ReplyKeyboardMarkup(
                keyboard=[
                    [
                        KeyboardButton(
                            text='🔥 Mahsulotlar',
                            web_app=WebAppInfo(url='https://uzum.uz')
                        ),
                        KeyboardButton(
                            text='📥Savat'
                        )
                        ],
                        [
                        KeyboardButton(
                            text='💼 Hamkorlik' 
                        ),
                        KeyboardButton(
                            text='ℹ️ Ma\'lumot'
                        )
                        ],
                        [
                        KeyboardButton(
                            text='🌐 Tilni tanlash'
                        )
                        ]
                ],
                resize_keyboard=True,
            )
        )
    else:
        update.message.reply_text(
            text=f"""Assalomu Alaykum, {update.message.from_user.first_name}!

Ijodimizga qiziqish bildirganingiz uchun tashakkur!

Hozircha siz uchun futbolka, xudi, svitshot, kepka va stikerlar mavjud. Yaqin orada tanlovni kengaytiramiz. Aytganday, istagan turdagi kiyim buyurtma berganlarlarga qo'shimcha ravishda stikerpak sovg'a qilinadi :)

Toshkent bo‘yicha yetkazib berish: 1–3 ish kuni
O‘zbekiston bo‘yicha yetkazib berish: 3–7 ish kuni
O‘zbekiston bo‘yicha jo‘natmalar seshanba va juma kunlari amalga oshiriladi

450 000 so'mdan ortiq buyurtmalarni yetkazib berish - tekin!

Agar bu shartlar sizni qoniqtirsa, “🔥 Mahsulotlar” bo'limiga o'tish orqali buyurtma berishni boshlashingiz mumkin.""",
            reply_markup=ReplyKeyboardMarkup(
                keyboard=[
                    [
                        KeyboardButton(
                            text='🔥 Mahsulotlar',
                            web_app=WebAppInfo(url='https://uzum.uz')
                        ),
                        KeyboardButton(
                            text='📥Savat'
                        )
                        ],
                        [
                        KeyboardButton(
                            text='💼 Hamkorlik' 
                        ),
                        KeyboardButton(
                            text='ℹ️ Ma\'lumot'
                        )
                        ],
                        [
                        KeyboardButton(
                            text='🌐 Tilni tanlash'
                        )
                        ]
                ],
                resize_keyboard=True,
            )
        )
    

def main_menu(update: Update, context: CallbackContext):
    update.message.reply_text(
                text=f"""Assalomu Alaykum, {update.message.from_user.first_name}!

Ijodimizga qiziqish bildirganingiz uchun tashakkur!

Hozircha siz uchun futbolka, xudi, svitshot, kepka va stikerlar mavjud. Yaqin orada tanlovni kengaytiramiz. Aytganday, istagan turdagi kiyim buyurtma berganlarlarga qo'shimcha ravishda stikerpak sovg'a qilinadi :)

Toshkent bo‘yicha yetkazib berish: 1–3 ish kuni
O‘zbekiston bo‘yicha yetkazib berish: 3–7 ish kuni
O‘zbekiston bo‘yicha jo‘natmalar seshanba va juma kunlari amalga oshiriladi

450 000 so'mdan ortiq buyurtmalarni yetkazib berish - tekin!

Agar bu shartlar sizni qoniqtirsa, “🔥 Mahsulotlar” bo'limiga o'tish orqali buyurtma berishni boshlashingiz mumkin.""",
                reply_markup=ReplyKeyboardMarkup(
                    keyboard=[
                        [
                        KeyboardButton(
                            text='🔥 Mahsulotlar',
                            web_app=WebAppInfo(url='https://uzum.uz')
                        ),
                         KeyboardButton(
                            text='📥Savat'
                        ), 
                        ],
                        [
                            KeyboardButton(
                            text='💼 Hamkorlik'
                        ),
                            KeyboardButton(
                            text='ℹ️ Ma\'lumot'
                        )    
                        ],
                        [
                        KeyboardButton(
                            text='🌐 Tilni tanlash'
                        )
                        ]
                    ],
                    resize_keyboard=True,
                )
            )

def order(update: Update, context: CallbackContext):
    context.user_data["state"] = "order"
    update.message.reply_text(
        text=f"Sizning savatingiz bo'sh"
        )
    
def about_us(update: Update, context: CallbackContext):
    context.user_data["state"] = "about_us"
    update.message.reply_text(
        text="""Biz sizning kompaniyangiz bilan hamkorlik qilishdan mamnunmiz va sizning buyurtmangizga\
            asosan futbolkalar, xudi, svitshot va boshqa ko'p narsalarni tayyorlashimiz mumkin.

Menejer bilan bog'lanish uchun: @tirik_chilik"""
        )

def show_info(update: Update, context: CallbackContext):
    context.user_data["state"] = "show_info"
    update.message.reply_text(
        text="Kerakli bo'limni tanlang ⬇️",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(
                    text='✍️ Izoh qoldirish'
                )
                ],
                [
                    KeyboardButton(
                       text='🚀 Yetkazib berish shartlari' 
                    ),
                    KeyboardButton(
                        text='☎️ Kontaktlar'
                    )
                ],
                [
                    KeyboardButton(
                        text='🏠 Bosh menyu'
                    )
                ]
                
            ],
            resize_keyboard=True,
        )
    )
 
def comment(update: Update, context: CallbackContext):
    context.user_data["state"] = "comment"
    update.message.reply_text(
        text=f"""✅ Tirikchilik loyihasini tanlaganingiz uchun rahmat.
Bizning xizmatlarimiz sifatini yaxshilashga yordam bersangiz juda xursand bo’lar edik :)
Buning uchun 5 ballik tizim asosida bizni baholang yoki o'z tilaklaringizni yozib jo'nating.""",
    reply_markup=ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(
                text='😊Menga hamma narsa yoqdi, 5 ❤️'
            )
            ],
            [
                KeyboardButton(
                    text='☺️Yaxshi, 4 ⭐️⭐️⭐️⭐️'
                )
            ],
            [
                KeyboardButton(
                    text='😐Qo\'niqarli, 3⭐️⭐️⭐️'
                )
            ],
            [
                KeyboardButton(
                    text='☹️Yoqmadi, 2 ⭐️⭐️'
                )
            ],
            [
                KeyboardButton(
                    text='😤Men shikoyat qilmoqchiman 👎🏻'
              )  
            ],
            [
                KeyboardButton(
                    text='🏠 Bosh menyu'
                )
            ]
        ],
        resize_keyboard=True,
    )
    )

def contact(update: Update, context: CallbackContext):
    update.message.reply_text(
        text="""Teskari aloqa uchun:
@tirik_chilik"""
    )
    
def sent_order(update: Update, context: CallbackContext):
    update.message.reply_text(
        text="""Yetkazib berish shartlari:
Toshkent bo‘yicha yetkazib berish: 1–3 ish kuni
O‘zbekiston bo‘yicha yetkazib berish: 3–7 ish kuni
O‘zbekiston bo‘yicha jo‘natmalar seshanba va juma kunlari amalga oshiriladi

Toshkent bo'ylab yetkazib berish - 30 000 so'm.
O‘zbekiston bo'ylab yetkazib berish - 40 000 so‘m.

450 000 so'mdan ortiq buyurtmalarni yetkazib berish - tekin!"""
    )
    
def like_bot(update: Update, context: CallbackContext):
    context.user_data["state"] = "like_bot"
    update.message.reply_text(
        text="""Mamnun qolganingizdan xursandmiz 😊. Siz va yaqinlaringizni
har doim xursand qilishga harakatamiz  qilamiz🤗""",
    reply_markup=ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(
                    text="⬅️ Orqaga"
                )
            ]
        ]
    )
    )
    
def good_bot(update: Update, context: CallbackContext):
    context.user_data["state"] = "good_bot"
    update.message.reply_text(
        text="""Sizga yoqqanidan xursandmiz 😊. Bot ishlashini yaxshilash uchun qanday maslahatlaringiz bor?👇🏻""",
    reply_markup=ReplyKeyboardMarkup(
    keyboard=[
            [
                KeyboardButton(
                    text="⬅️ Orqaga"
                )
            ]
        ]
    )
    )

def satisfactory_bot(update: Update, context: CallbackContext):
    context.user_data["state"] = "satisfactory_bot"
    update.message.reply_text(
        text="""Botimiz sizni qoniqtirmaganidan afsusdamiz 😔. 
Bizni yaxshilashga yordam bering, 
sharh va takliflaringizni qoldiring👇🏻. 
Yaxshilashga harakat qilamiz🙏🏻.""",
    reply_markup=ReplyKeyboardMarkup(
    keyboard=[
            [
                KeyboardButton(
                    text="⬅️ Orqaga"
                )
            ]
        ]
    )
    )
    
def not_like_bot(update: Update, context: CallbackContext):
    context.user_data["state"] = "not_like_bot"
    update.message.reply_text(
        text="""Botimiz sizni qoniqtirmaganidan afsusdamiz 😔. 
Bizni yaxshilashga yordam bering, sharh va takliflaringizni qoldiring👇🏻.
Yaxshilashga harakat qilamiz🙏🏻""",
    reply_markup=ReplyKeyboardMarkup(
    keyboard=[
            [
                KeyboardButton(
                    text="⬅️ Orqaga"
                )
            ]
        ]
    )
    )
    
def complaint_bot(update: Update, context: CallbackContext):
    context.user_data["state"] = "complaint_bot"
    update.message.reply_text(
        text="""Botimiz sizni qoniqtirmaganidan afsusdamiz 😔. 
Bizni yaxshilashga yordam bering, sharh va takliflaringizni qoldiring👇🏻. 
Yaxshilashga harakat qilamiz🙏🏻""",
    reply_markup=ReplyKeyboardMarkup(
    keyboard=[
            [
                KeyboardButton(
                    text="⬅️ Orqaga" 
                )
            ]
        ]
    )
    )
    
def back(update: Update, context: CallbackContext):
    text = update.message.text
    if text == "⬅️ Orqaga":
        current_state = context.user_data.get("state")
        
        if current_state == "settings":
            main_menu(update, context)
        
        elif current_state == "order":
            main_menu(update, context)
            
        elif current_state == "about_us":
            main_menu(update, context)
            
        elif current_state == "coment":
            main_menu(update, context)
        
        elif current_state == "like_bot":
            comment(update, context)
            
        elif current_state == "good_bot":
            comment(update, context)
            
        elif current_state == "satisfactory_bot":
            comment(update, context)
            
        elif current_state == "not_like_bot":
            comment(update, context)
            
        elif current_state == "complaint_bot":
            comment(update, context)