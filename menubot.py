from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8825921982:AAE6KP8SgXcOAzf7DbgsgIs5eTeixxXuhLQ"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🛍️ My Services", callback_data='services')],
        [InlineKeyboardButton("⭐ Reviews", callback_data='reviews')],
        [InlineKeyboardButton("📞 Contact Me", callback_data='contact')],
        [InlineKeyboardButton("❓ How to Order?", callback_data='how')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Welcome to Menu Bot EG 🤖\n\n"
        "I create professional Telegram bots with menus\n"
        "Fast, secure & auto-manage your group ✨\n\n"
        "Choose from the menu below:",
        reply_markup=reply_markup
    )

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == 'services':
        text = (
            "🔥 My Services:\n\n"
            "1️⃣ Professional Menu Bot (Arabic/English)\n"
            "2️⃣ Anti-Spam & Link Protection\n"
            "3️⃣ Auto Welcome Message\n"
            "4️⃣ Google Sheets Integration\n\n"
            "Starting from $10 only!"
        )
    elif query.data == 'reviews':
        text = "⭐⭐⭐⭐⭐\n\n\"Amazing bot, super fast!\" - Ahmed\n\"My group is now secure\" - Sarah\n\nJoin my happy clients!"
    elif query.data == 'contact':
        text = "📞 Contact:\n\nTelegram: @YourUsername\nFiverr: @zoza_labs"
    elif query.data == 'how':
        text = "📝 How to order?\n\n1. Send me your bot idea\n2. I send price & time\n3. Get your bot same day!"

    keyboard = [[InlineKeyboardButton("🔙 Back to Menu", callback_data='back')]]
    if query.data == 'back':
        await start(update, context)
        return
        
    await query.edit_message_text(text, reply_markup=InlineKeyboardMarkup(keyboard))

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(buttons))
print("Bot is running...")
app.run_polling()
