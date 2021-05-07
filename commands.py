import telegram
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

def start(update, context):
    update.message.reply_text("Ha iniciado conversación con el bot.")

def get_arguments(update, context):
    text = update.message.text
    print(text)
    text = text.replace("/argumentos", "")
    update.message.reply_text("Los argumentos fueron" + text)

def send_photo(update, context):

    chat_id = update.message.chat.id
    # archivo
    img = open('./beholder.png', 'rb')
    # Enviar imagen
    context.bot.send_photo(chat_id, photo=img)
    update.message.reply_text("uuuuh scary beholder")

def options(update: telegram.Update, context):
    texto = update.message.text  # /teclado n m
    texto = texto[len('/teclado')+1:]
    texto = texto.split(" ")
    if len(texto) != 3:
        update.message.reply_text("Digite parámetros n, m, p válidos. Separados por un espacio.")
    else:
        n, K, p = int(texto[0]), int(texto[1]), int(texto[2])
        options = [
            [
                InlineKeyboardButton("Distribuir", callback_data="1"),
                InlineKeyboardButton("Cadenas", callback_data="2"),
            ],
            [InlineKeyboardButton("pcadenas", callback_data="3"),
             InlineKeyboardButton("Histograma", callback_data="4")]
        ]

        reply_markup = InlineKeyboardMarkup(options)

        update.message.reply_text('Elija una opción:', reply_markup=reply_markup)


def callback_handler(update, context):
    query = update.callback_query
    query.answer()
    data = query.data
    update.message.reply_text("opcion" + data)
 