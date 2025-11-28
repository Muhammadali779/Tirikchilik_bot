from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from config import Config
from handlers import (start, about_us, order, show_info, main_menu, 
comment, like_bot, back, good_bot, satisfactory_bot, not_like_bot,
complaint_bot, sent_order, contact)


def main() -> None:
    updater = Updater(Config.TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(
        handler=CommandHandler(
            command='start',
            callback=start
        )
    )
    
    dispatcher.add_handler(
        handler=MessageHandler(
            filters=Filters.text('💼 Hamkorlik'),
            callback=about_us
        )
    )
    
    dispatcher.add_handler(
       handler=MessageHandler(
           filters=Filters.text('📥Savat'),
           callback=order
       ) 
    )
    dispatcher.add_handler(
        handler=MessageHandler(
            filters=Filters.text('ℹ️ Ma\'lumot'),
            callback=show_info
        )
    )
    dispatcher.add_handler(
        handler=MessageHandler(
            filters=Filters.text('🏠 Bosh menyu'),
            callback=main_menu
        )
    )
    dispatcher.add_handler(
        handler=MessageHandler(
            filters=Filters.text('✍️ Izoh qoldirish'),
            callback=comment
        )
    )
    dispatcher.add_handler(
        handler=MessageHandler(
            filters=Filters.text('😊Menga hamma narsa yoqdi, 5 ❤️'),
            callback=like_bot
        )
    )
    dispatcher.add_handler(
        handler=MessageHandler(
            filters=Filters.text("⬅️ Orqaga"),
            callback=back
        )
    )
    dispatcher.add_handler(
        handler=MessageHandler(
            filters=Filters.text('☺️Yaxshi, 4 ⭐️⭐️⭐️⭐️'),
            callback=good_bot
        )
    )
    dispatcher.add_handler(
        handler=MessageHandler(
            filters=Filters.text('😐Qo\'niqarli, 3⭐️⭐️⭐️'),
            callback=satisfactory_bot
        )
    )
    dispatcher.add_handler(
        handler=MessageHandler(
            filters=Filters.text('☹️Yoqmadi, 2 ⭐️⭐️'),
            callback=not_like_bot
        )
    )
    dispatcher.add_handler(
        handler=MessageHandler(
            filters=Filters.text('😤Men shikoyat qilmoqchiman 👎🏻'),
            callback=complaint_bot
        )
    )
    dispatcher.add_handler(
        handler=MessageHandler(
            filters=Filters.text('🚀 Yetkazib berish shartlari'),
            callback=sent_order
        )
    )
    dispatcher.add_handler(
        handler=MessageHandler(
            filters=Filters.text('☎️ Kontaktlar'),
            callback=contact
        )
    )
 
 

    updater.start_polling()
    updater.idle()

main()