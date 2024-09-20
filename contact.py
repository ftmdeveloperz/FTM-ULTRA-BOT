from telegram import Update
from telegram.ext import CallbackContext

def contact_developer(update: Update, context: CallbackContext):
    """Provide contact information for the developer."""
    contact_message = (
        "For support or inquiries, contact the developer:\n"
        "@ftmdeveloper"
    )
    update.message.reply_text(contact_message)
