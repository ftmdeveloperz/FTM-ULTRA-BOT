from telegram import Update
from telegram.ext import CallbackContext
def send_bot_status():
    return "Bot is running smoothly!"
def notify_user(update: Update, context: CallbackContext, message: str):
    """Send a notification to the user."""
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)
