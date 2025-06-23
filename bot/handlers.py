from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from bot.cwallet_monitor import handle_cwallet_message
from config import BOT_TOKEN
from database import setup_db

async def start(update, context):
    await update.message.reply_text("🤖 Welcome to DegenCred! Use /loan to request your first loan.")

async def txalert(update, context):
    db_pool = context.bot_data.get("db_pool")
    if update.message.reply_to_message:
        await handle_cwallet_message(update.message.reply_to_message, db_pool)
        await update.message.reply_text("📦 Processing transaction...")

def setup_handlers():
    app = ApplicationBuilder().token(BOT_TOKEN).post_init(post_init).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("txalert", txalert))
    app.add_handler(MessageHandler(filters.ALL, lambda u, c: None))  # placeholder
    app.run_polling()

async def post_init(app):
    db_pool = await setup_db()
    app.bot_data["db_pool"] = db_pool
