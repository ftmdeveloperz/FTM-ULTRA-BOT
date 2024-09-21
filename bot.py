import logging
import moviepy.editor as mp
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from config import BOT_TOKEN
from premium_management import add_premium_user, remove_premium_user
from about import about_info
from contact import contact_developer
from id_extractor import extract_id
from clone import clone_bot
from notifications import send_bot_status

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Function to merge videos
def merge_videos(video_paths, output_path):
    try:
        clips = [mp.VideoFileClip(video) for video in video_paths]
        final_clip = mp.concatenate_videoclips(clips)
        final_clip.write_videofile(output_path)
        return output_path
    except Exception as e:
        return f"An error occurred while merging videos: {e}"

# Function to trim a video
def trim_video(video_path, start_time, end_time, output_path):
    try:
        video = mp.VideoFileClip(video_path).subclip(start_time, end_time)
        video.write_videofile(output_path)
        return output_path
    except Exception as e:
        return f"An error occurred while trimming the video: {e}"

# Function to improve video quality
def improve_video_quality(input_path, output_path, resolution='720p'):
    try:
        video = mp.VideoFileClip(input_path)
        video = video.resize(height=720)  # Adjust resolution
        video.write_videofile(output_path)
        return output_path
    except Exception as e:
        return f"An error occurred while improving video quality: {e}"

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
        "/mergevideos <list_of_paths> - Merge multiple videos\n"
        "/trimvideo <video_path> <start_time> <end_time> - Trim a video\n"
        "/improvequality <video_path> - Improve video quality\n"
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

async def merge_videos_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    video_paths = context.args
    if not video_paths:
        await update.message.reply_text("Please provide paths to the videos to merge.")
        return
    
    output_path = "output_merged.mp4"  # Customize this as needed
    result = merge_videos(video_paths, output_path)
    await update.message.reply_text(result)

async def trim_video_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 3:
        await update.message.reply_text("Usage: /trimvideo <video_path> <start_time> <end_time>")
        return
    video_path, start_time, end_time = context.args
    output_path = "output_trimmed.mp4"  # Customize this as needed
    result = trim_video(video_path, start_time, end_time, output_path)
    await update.message.reply_text(result)

async def improve_quality_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) < 1:
        await update.message.reply_text("Usage: /improvequality <video_path>")
        return
    video_path = context.args[0]
    output_path = "output_improved.mp4"  # Customize this as needed
    result = improve_video_quality(video_path, output_path)
    await update.message.reply_text(result)

async def clone(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        bot_token = context.args[0]
        await clone_bot(update, bot_token)
    else:
        await update.message.reply_text("Please provide the bot token.")

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    status_message = send_bot_status()
    await update.message.reply_text(status_message)

# Main function to start the bot
async def main():
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Register command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("about", about))
    application.add_handler(CommandHandler("contact", contact))
    application.add_handler(CommandHandler("extractid", extract_user_id))
    application.add_handler(CommandHandler("mergevideos", merge_videos_command))
    application.add_handler(CommandHandler("trimvideo", trim_video_command))
    application.add_handler(CommandHandler("improvequality", improve_quality_command))
    application.add_handler(CommandHandler("clone", clone))
    application.add_handler(CommandHandler("status", status))

    # Start the bot
    await application.run_polling()

if __name__ == '__main__':
    asyncio.run(main())  # Use asyncio.run to start the bot
