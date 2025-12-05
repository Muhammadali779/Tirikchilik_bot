from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler, filters
)
from config import Config
from handlers import (
    start, about_us, order, show_info, main_menu,
    comment, like_bot, back, good_bot, satisfactory_bot,
    not_like_bot, complaint_bot, sent_order, contact
)


def main():
    app = ApplicationBuilder().token(Config.TOKEN).build()

    # /start
    app.add_handler(CommandHandler("start", start))

    # Matnli tugmalar
    app.add_handler(MessageHandler(filters.Text("💼 Hamkorlik"), about_us))
    app.add_handler(MessageHandler(filters.Text("📥Savat"), order))
    app.add_handler(MessageHandler(filters.Text("ℹ️ Ma'lumot"), show_info))
    app.add_handler(MessageHandler(filters.Text("🏠 Bosh menyu"), main_menu))
    app.add_handler(MessageHandler(filters.Text("✍️ Izoh qoldirish"), comment))
    app.add_handler(MessageHandler(filters.Text("😊Menga hamma narsa yoqdi, 5 ❤️"), like_bot))
    app.add_handler(MessageHandler(filters.Text("⬅️ Orqaga"), back))
    app.add_handler(MessageHandler(filters.Text("☺️Yaxshi, 4 ⭐️⭐️⭐️⭐️"), good_bot))
    app.add_handler(MessageHandler(filters.Text("😐Qo'niqarli, 3⭐️⭐️⭐️"), satisfactory_bot))
    app.add_handler(MessageHandler(filters.Text("☹️Yoqmadi, 2 ⭐️⭐️"), not_like_bot))
    app.add_handler(MessageHandler(filters.Text("😤Men shikoyat qilmoqchiman 👎🏻"), complaint_bot))
    app.add_handler(MessageHandler(filters.Text("🚀 Yetkazib berish shartlari"), sent_order))
    app.add_handler(MessageHandler(filters.Text("☎️ Kontaktlar"), contact))

    print("Bot ishga tushdi...")
    app.run_polling()


if __name__ == "__main__":
    main()
