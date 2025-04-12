import telebot
import requests
import time
import random
import os

BOT_TOKEN = os.getenv("BOT_TOKEN", "")

bot = telebot.TeleBot(BOT_TOKEN)

loading_bar = [
    "[■□□□□□□□□□] 10%",
    "[■■□□□□□□□□] 20%",
    "[■■■□□□□□□□] 30%",
    "[■■■■□□□□□□] 40%",
    "[■■■■■□□□□□] 50%",
    "[■■■■■■□□□□] 60%",
    "[■■■■■■■□□□] 70%",
    "[■■■■■■■■□□] 80%",
    "[■■■■■■■■■□] 90%",
    "[■■■■■■■■■■] 100%"
]

connecting_steps = [
    "🔍 Connecting to Server...",
    "🔓 Injecting Email Fingerprint...",
    "🧠 Initializing Deep Breach Scan...",
    "🛡️ Bypassing Leak Firewalls...",
    "🧬 Decrypting Data Nodes...",
    "✅ Access Granted"
]

@bot.message_handler(commands=['start'])
def welcome(msg):
    bot.send_message(msg.chat.id,
    "╔════════════════════════════╗\n"
    "     🚨 Email Breach Scanner 🚨\n"
    "╚════════════════════════════╝\n\n"
    "💬 *Send any email to begin deep scan.*\n"
    "_Use for Educational Purpose Only._\n\n"
    "🔗 [CrackA on Facebook](https://www.facebook.com/cracka56)\n"
    "👨‍💻 *Developed by CrackA*", parse_mode="Markdown")

@bot.message_handler(func=lambda m: '@' in m.text)
def scan_email(message):
    email = message.text.strip()
    chat_id = message.chat.id

    # Connecting animation
    con_msg = bot.send_message(chat_id, "Initializing...", parse_mode="Markdown")
    for step in connecting_steps:
        bot.edit_message_text(f"`{step}`", chat_id, con_msg.message_id, parse_mode="Markdown")
        time.sleep(0.8)

    # Loading bar
    load_msg = bot.send_message(chat_id, "`[□□□□□□□□□□] 0%`", parse_mode="Markdown")
    for frame in loading_bar:
        bot.edit_message_text(f"`{frame}`", chat_id, load_msg.message_id, parse_mode="Markdown")
        time.sleep(0.3)
    bot.delete_message(chat_id, load_msg.message_id)

    bot.send_message(chat_id, f"🎯 *Scanning Email:* `{email}`", parse_mode="Markdown")

    # API Call
    api = f"https://leakcheck.io/api/public?check={email}"
    try:
        r = requests.get(api)
        data = r.json()

        if data.get("found", 0) > 0:
            msg = f"⚠️ `{email}` Found in *{data['found']}* Breach(es):\n\n"
            for src in data.get("sources", []):
                msg += f"• `{src}`\n"
            msg += "\n⚠️ _Change your passwords immediately!_\n\n🔗 [CrackA on Facebook](https://www.facebook.com/cracka56)\n👨‍💻 *Developed by CrackA*"
        else:
            msg = f"✅ `{email}` is *Safe*. No data breach found.\n\n🔗 [CrackA on Facebook](https://www.facebook.com/cracka56)\n👨‍💻 *Developed by CrackA*"

    except Exception as e:
        msg = f"❌ *Error while scanning:*\n`{str(e)}`"

    bot.send_message(chat_id, msg, parse_mode="Markdown")

bot.polling()
