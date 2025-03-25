from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Bot Token (Replace with your actual bot token)
BOT_TOKEN = "7868332753:AAEp5Z6FNb4G7YdqiYAb0xSbrGDP0qczI2Q"

# APK file path (Ensure this file exists in the script's directory)
APK_FILE_PATH = "loader.apk"

# Secret Key (Set your custom key here)
SECRET_KEY = "DM - @ARPIT_OP"

# MOD APK Download Link (Set your mod apk link here)
MOD_APK_LINK = "https://t.me/c/1905205736/3313"  # <-- Yahan apni MOD APK link daalein

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Hello! Use:\n"
        "/giveloader - Get Loader APK\n"
        "/key - Get Your Key\n"
        "/modapk - Get Mod APK Link"
    )

async def send_loader(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.message.chat_id
    try:
        # Open the APK file and send it to the user
        with open(APK_FILE_PATH, "rb") as apk:
            await context.bot.send_document(chat_id=chat_id, document=apk, caption="Here is your loader APK!")
    except FileNotFoundError:
        await update.message.reply_text("Sorry, the APK file could not be found. Please ensure 'loader.apk' is in the same directory as this script.")

async def send_key(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends the predefined secret key to the user."""
    await update.message.reply_text(f"Your Key: {SECRET_KEY}", parse_mode="Markdown")

async def send_modapk(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends the mod apk download link to the user."""
    await update.message.reply_text(f"Download the Mod APK here: [Click Here]({MOD_APK_LINK})", parse_mode="Markdown")

def main():
    # Create the bot application
    application = Application.builder().token(BOT_TOKEN).build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("giveloader", send_loader))
    application.add_handler(CommandHandler("key", send_key))
    application.add_handler(CommandHandler("modapk", send_modapk))  # Added modapk command

    # Start the bot
    application.run_polling()

if __name__ == "__main__":
    main()