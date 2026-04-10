import os
from telegram import Update
from telegram.ext import Application, CommandHandler

TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context):
    await update.message.reply_text("⚔️ BIENVENUE SUR MINI ZETSU ! ⚔️")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
