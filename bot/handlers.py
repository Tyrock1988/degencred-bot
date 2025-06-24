from telegram.ext import CommandHandler, MessageHandler, filters, Application
from bot.cwallet_monitor import handle_cwallet_message
from database import setup_db

# Commands
async def start(update, context):
    await update.message.reply_text("🤖 Welcome to DegenCred! Use /loan to request your first loan.")

async def txalert(update, context):
    db_pool = context.bot_data.get("db_pool")
    if update.message.reply_to_message:
        await handle_cwallet_message(update.message.reply_to_message, db_pool)
        await update.message.reply_text("📦 Processing transaction...")

# Called by main.py — injects your handlers into the bot instance
def setup_handlers(app: Application):
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("txalert", txalert))
    app.add_handler(MessageHandler(filters.ALL, lambda u, c: None))  # placeholder

    app.post_init = post_init  # Register db setup

# Called when the bot starts
async def post_init(app: Application):
    db_pool = await setup_db()
    app.bot_data["db_pool"] = db_pool
