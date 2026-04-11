import os
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler

TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context):
    await update.message.reply_text("⚔️ BIENVENUE SUR MINI ZETSU ! ⚔️")

async def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    
    # Supprime tout webhook existant
    await app.bot.delete_webhook()
    
    print("🤖 Mini Zetsu en ligne !")
    await app.run_polling(allowed_updates=["message"])

if __name__ == "__main__":
    asyncio.run(main())
