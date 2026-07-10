from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8959588177:AAFZL10qR_mDhVwemSnD5mYXcRuAlpl5Bps"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Atlas-OS is running 🚀")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - Start the bot\n"
        "/help - Show available commands"
    )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()