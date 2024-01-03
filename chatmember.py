#!/usr/bin/env python
# pylint: disable=unused-argument
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to handle '(my_)chat_member' updates.
Greets new users & keeps track of which chats the bot is in.

Usage:
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""
import sqlite3
import logging
import os
from typing import Optional, Tuple

from telegram import Chat, ChatMember, ChatMemberUpdated, Update, ReplyKeyboardMarkup
from telegram.constants import ParseMode
from telegram.ext import (
    Application,
    ChatMemberHandler,
    CommandHandler,
    ConversationHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

from pprint import pprint

TOKEN = os.getenv("TELEGRAM_TOKEN")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)


DISP = 0
NOME_REMEDIO = 1
CONFIRMACAO_REMEDIO = 2 

async def start_private_chat(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    user_name = update.effective_user.full_name
    chat = update.effective_chat

    if chat.type != Chat.PRIVATE or chat.id in context.bot_data.get("user_ids", set()):
        return None

    logger.info("%s started a private chat with the bot", user_name)
    context.bot_data.setdefault("user_ids", set()).add(chat.id)

    await update.effective_message.reply_text(
        f"Bem vindo{user_name}. Caso queira receber atualizacoes dos remedios disponiveis, digite /disp"
    )


async def disp(update : Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Regista para receber as atualizações de medicamento"""
    print(update)

    reply_keyboard = [["Ceilândia", "Asa Sul", "Gama"]]
    
    await update.message.reply_text(
        "Olá vou te ajudar a encontrar se o seu remédio está disponível. Escolha qual cidade tem interesse:",
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard,one_time_keyboard=True, input_field_placeholder="Qual cidade?"
        )
    )
    
    #await context.bot.send_message(chat_id= update.effective_chat.id,text = " teste")

    return NOME_REMEDIO

async def nome_remedio(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:

    user = update.message.from_user
    medicine_local = update.message.text

    logger.info(f"usuario {user} escolheu {medicine_local}")

    await update.message.reply_text(
        "me diga agora qual remedio voce tem interesse : "
    )

    return CONFIRMACAO_REMEDIO



async def confirmacao_remedio(update : Update, context: ContextTypes.DEFAULT_TYPE) -> int:

    nome_remedio = update.message.text

    logger.info(f" usuario falou que o remedio era {nome_remedio}")




def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int: 



    pass


def main() -> None:
    """Start the bot."""
    application = Application.builder().token(TOKEN).build()
    application.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, start_private_chat))

    #disp_handler = CommandHandler("disp", disp)

    #application.add_handler(disp_handler)

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("disp", disp)],
        states={
            DISP: [ MessageHandler(filters.Regex("^(Ceilândia|Asa sul|Gama)$"), disp)  ],
            NOME_REMEDIO : [MessageHandler(filters.Regex(r"\w"), nome_remedio), ],
            CONFIRMACAO_REMEDIO : [MessageHandler(filters.ALL, confirmacao_remedio)]
        }
        ,fallbacks=[CommandHandler("cancel", cancel)]
    )

    application.add_handler(conv_handler)


    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()