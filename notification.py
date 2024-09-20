from telegram import Update
from telegram.ext import CallbackContext

def notify_user(update: Update, context: CallbackContext, message: str):
    """Send a notification to the user."""
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)
