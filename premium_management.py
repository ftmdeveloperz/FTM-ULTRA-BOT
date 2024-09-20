from telegram import Update
from telegram.ext import CallbackContext
from config import PREMIUM_USER_IDS
from utils import log_activity, handle_error, send_message

def add_premium_user(update: Update, context: CallbackContext):
    """Add a user to the premium list."""
    try:
        if update.effective_user.id == context.bot.owner_id:
            user_id = int(context.args[0])
            duration = int(context.args[1])  # Duration in days
            PREMIUM_USER_IDS.append(user_id)
            log_activity(f"Added user {user_id} as premium for {duration} days.")
            send_message(update, context, f"User {user_id} has been added as a premium user for {duration} days.")
        else:
            send_message(update, context, "You are not authorized to add premium users.")
    except Exception as e:
        handle_error(e)
        send_message(update, context, "An error occurred while adding the premium user.")

def check_premium_status(user_id):
    """Check if a user is premium."""
    return user_id in PREMIUM_USER_IDS

def remove_premium_user(update: Update, context: CallbackContext):
    """Remove a user from the premium list."""
    try:
        if update.effective_user.id == context.bot.owner_id:
            user_id = int(context.args[0])
            if user_id in PREMIUM_USER_IDS:
                PREMIUM_USER_IDS.remove(user_id)
                log_activity(f"Removed user {user_id} from premium list.")
                send_message(update, context, f"User {user_id} has been removed from the premium list.")
            else:
                send_message(update, context, f"User {user_id} is not a premium user.")
        else:
            send_message(update, context, "You are not authorized to remove premium users.")
    except Exception as e:
        handle_error(e)
        send_message(update, context, "An error occurred while removing the premium user.")
