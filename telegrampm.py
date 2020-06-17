from telegram.ext import Updater,CommandHandler
from telegram import InlineKeyboardButton,InlineKeyboardMarkup
from telegram.ext import CallbackQueryHandler
from telegram.ext import MessageHandler
#insert your id as a admin of the bot
id_admin=344254169
#insert your bot token
tokenbot='1198163289:AAHxc_PaAje8vAYRiatpvtRkG2f5i8P0q8M'
#leave this 3 variable empty------
pm=""
sender=""
userinfo=""
#---------------------------------
updater=Updater(tokenbot)
def start(bot,update):
    bot.send_message(chat_id=update.message.chat_id,text="by this command /pm send your message")
    #print(update.message)
def getpm(bot,update,args):
    global pm
    global sender
    global userinfo
    pm=" ".join(args[0:])
    bot.send_message(chat_id=update.message.chat_id,text="📤Your message was sent to the admin!")
    sender=update.message.chat.username
    userinfo=update.message.chat_id
    #bot.send_message(chat_id=344254169,text=f'📩payam jadidi darid\n🎯@{update.message.chat.username} send this message:\n✏️{pm}')
    keyboard=[[InlineKeyboardButton(text="show message",callback_data='1')]]     
    bot.send_message(text="you have a new message",chat_id=id_admin,reply_markup=InlineKeyboardMarkup(keyboard))
def halmer(bot,update):
    global pm
    query=update.callback_query
    data=query.data
    #chat_id=query.message.chat_id
    message_id=query.message.message_id
    bot.editMessageText(text=f'📩your message\n🎯@{sender},id={userinfo} send this message:\n✏️{pm}',chat_id=id_admin,message_id=message_id)
def pm_to_user(bot,update,args):
    '''answer to user by admin'''
    user=args[0]
    pm=" ".join(args[1:])
    if user.isdigit()==False:
        bot.send_message(chat_id=id_admin,text="id should be a number")
    elif user.isdigit()==True:
        if len(str(user))==9:
            bot.send_message(chat_id=user,text=pm)
            bot.send_message(chat_id=id_admin,text="Your answer has been sent")
        else:
            bot.send_message(chat_id=id_admin,text="id is wrong")
updater.dispatcher.add_handler(CommandHandler("start",start))
updater.dispatcher.add_handler(CommandHandler("pm",getpm,pass_args=True))
updater.dispatcher.add_handler(CommandHandler("answer",pm_to_user,pass_args=True))
updater.dispatcher.add_handler(CallbackQueryHandler(halmer))
updater.start_polling()
updater.idle()
