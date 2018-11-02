import telegram
bot = telegram.Bot("693502652:AAEuMUTlTnxiUzs3iguaHRZ7Ma62unjcEnk")

import logging
from telegram.ext import Updater, CommandHandler
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

def meatcake(bot, update):
    update.message.reply_text(" @Trainer_Jono 's daughter")

def jono(bot, update):
    update.message.reply_text("is mother")

def peachy(bot, update):
    update.message.reply_text(" @krystine_j ")

def bb(bot, update):
    update.message.reply_text(" @ijustmeatyou ")

def me(bot, update):
    update.message.reply_text(" @meatcake ")

updater = Updater(token="693502652:AAEuMUTlTnxiUzs3iguaHRZ7Ma62unjcEnk")
dp = updater.dispatcher
dp.add_handler(CommandHandler("meatcake", meatcake))
dp.add_handler(CommandHandler("jono", jono))
dp.add_handler(CommandHandler("peachy", peachy))
dp.add_handler(CommandHandler("whereisourcmder", bb))
dp.add_handler(CommandHandler("commanderrr", me))
updater.start_polling()


