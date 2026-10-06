import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

# লগিং সেটআপ
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# /start কমান্ড: বটের সাথে পরিচয়
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(
        f"✨ *Hello {user.first_name}! Welcome to Elite System.*\n\n"
        f"👑 *OWNER:* 🦋⃟ᴠͥɪͣᴘͫ♔ S̴O̴J̴I̴B̴—͟͞͞ O̴W̴N̴E̴R̴\n\n"
        "আপনার আইডি বের করতে /info লিখুন。",
        parse_mode='Markdown'
    )

# /info কমান্ড: ইউজারের আইডি এবং নাম বের করা
async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    user_id = user.id
    username = user.username if user.username else "N/A"
    
    response = (
        f"⚙️ **ব্যবহারকারীর তথ্য:**\n\n"
        f"👤 নাম: {user.first_name}\n"
        f"🆔 আইডি: `{user_id}`\n"
        f"🏷 ইউজারনেম: @{username}\n\n"
        f"এই আইডিটি সাকসেসফুলি ডিটেক্ট করা হয়েছে।"
    )
    await update.message.reply_text(response, parse_mode='Markdown')

if __name__ == '__main__':
    # আপনার দেওয়া টোকেনটি এখানে বসানো হয়েছে
    TOKEN = "8719896989:AAH-LbIboHggDoUwRbLdSFBGed9-ihYFTlA"
    
    # অ্যাপ বিল্ড করা
    app = ApplicationBuilder().token(TOKEN).build()
    
    # হ্যান্ডলার যুক্ত করা (block=False এর ফলে প্যারালাল রেসপন্স ফাস্ট হবে)
    app.add_handler(CommandHandler("start", start, block=False))
    app.add_handler(CommandHandler("info", info, block=False))
    
    print("🚀 ARIYAN BD Official Bot এখন লাইভ হয়েছে...")
    print("বটটি সক্রিয় করতে টার্মিনালে রান করুন এবং টেলিগ্রামে গিয়ে মেসেজ দিন।")
    
    # বট রান করা (পুরনো পেন্ডিং আপডেট বাদ দিয়ে দ্রুত রান করবে)
    app.run_polling(drop_pending_updates=True)
