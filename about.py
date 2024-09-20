from telegram import Update
from telegram.ext import CallbackContext
def about_info():
    return "FTM ULTRA BOT is designed to process and manage media files efficiently."
def about(update: Update, context: CallbackContext):
    """Send information about the bot."""
    about_message = (
        "FTM ULTRA BOT is a powerful media processing bot for Telegram.\n"
        "Features include:\n"
        "- Merge and trim audio and video files\n"
        "- Improve quality of media files\n"
        "- Support for multiple formats\n"
        "- Premium subscription options\n"
        "For more information, contact @ftmdeveloper."
    )
    update.message.reply_text(about_message)
