import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Import your other modules
from config import TOKEN
from process import handle_process
from premium_management import add_premium_user, remove_premium_user
from about import about_info
from contact import contact_developer
from id_extractor import extract_id
from clone import clone_bot

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Command Handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to FTM ULTRA BOT! Use /help to see available commands.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
        "/start - Start the bot\n"
        "/addpremium <user_id> <duration_in_days> - Add a premium user\n"
        "/removepremium <user_id> - Remove a premium user\n"
        "/about - About this bot\n"
        "/contact - Contact the developer\n"
        "/extractid - Extract your user ID\n"
        "/clone <bot_token> - Clone the bot\n"
        "/status - Check bot status"
    )
    await update.message.reply_text(help_text)

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(about_info())

async def contact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(contact_developer())

async def extract_user_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = extract_id(update)
    await update.message.reply_text(f"Your User ID is: {user_id}")

async def clone(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        bot_token = context.args[0]
        await clone_bot(update, bot_token)
    else:
        await update.message.reply_text("Please provide the bot token.")

# Main function to start the bot
async def main():
    application = ApplicationBuilder().token(TOKEN).build()

    # Register handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("about", about))
    application.add_handler(CommandHandler("contact", contact))
    application.add_handler(CommandHandler("extractid", extract_user_id))
    application.add_handler(CommandHandler("clone", clone))
    # Add premium management commands as needed

    # Start the bot
    await application.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
