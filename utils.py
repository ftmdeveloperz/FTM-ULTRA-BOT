import logging

# Configure logging
logging.basicConfig(
    filename='bot.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_activity(message):
    """Log a message to the bot log file."""
    logging.info(message)

def handle_error(error):
    """Log an error message to the bot log file."""
    logging.error(f"An error occurred: {error}")

def send_message(update, context, message):
    """Send a message to a user or group chat."""
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)
