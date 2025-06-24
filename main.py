from fastapi import FastAPI, Request
import asyncio
import uvicorn
import os

from telegram import Update
from telegram.ext import Application, CommandHandler
from bot.handlers import setup_handlers
from config import load_config

app = FastAPI()
config = load_config()

# Create Telegram bot application
telegram_app = Application.builder().token(config.BOT_TOKEN).build()
setup_handlers(telegram_app)

@app.get("/")
def health_check():
    return {"status": "ok"}

@app.get("/health")
def detailed_health_check():
    return {"status": "degencred bot online", "webhook": True}

@app.post("/webhook")
async def telegram_webhook(request: Request):
    data = await request.json()
    update = Update.de_json(data, telegram_app.bot)
    await telegram_app.process_update(update)
    return {"ok": True}

# Start FastAPI + Telegram in webhook mode
if __name__ == "__main__":
    async def run():
        await telegram_app.initialize()
        await telegram_app.bot.set_webhook(url="https://degencred-bot.fly.dev/webhook")
        await telegram_app.start()
        uvicorn.run(app, host="0.0.0.0", port=8080)

    asyncio.run(run())
