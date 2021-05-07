#https://python-telegram-bot.readthedocs.io/en/stable/
#
# Documentacion bots
from telegram.ext import Updater, CommandHandler, MessageHandler,  CallbackQueryHandler
import commands

url = "https://web.telegram.org/#/im?p=@Arvis_Bot"
api_key = "1840690866:AAERIsIVGGDTo0dnIvk9BSqN9RN5ckTmIYg"

def main():
    updater = Updater(api_key, use_context=True)

    dispatcher = updater.dispatcher

    # se aaden los métodos que controlan cada comando

    # mensajes de texto
    dispatcher.add_handler(CommandHandler('start', commands.start))
    dispatcher.add_handler(CommandHandler('argumentos', commands.get_arguments))


    dispatcher.add_handler(CommandHandler('send_photo', commands.send_photo))
    dispatcher.add_handler(CommandHandler('options', commands.options))
    dispatcher.add_handler(CallbackQueryHandler(commands.callback_handler))

    # dispatcher.add_handler(CommandHandler('teclado', bot1.teclado))
    # dispatcher.add_handler(CallbackQueryHandler(bot1.opcion))



    # dispatcher.add_handler(CommandHandler('foto', bot1.foto))


    updater.start_polling()
    updater.idle()

main()