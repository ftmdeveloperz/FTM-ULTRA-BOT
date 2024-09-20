from telegram import Update
from telegram.ext import CallbackContext

def extract_id(update: Update, context: CallbackContext):
    """Extract and send the user ID of the message sender."""
    user_id = update.effective_user.id
    update.message.reply_text(f"Your user ID is: {user_id}")
