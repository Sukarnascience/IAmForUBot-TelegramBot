from telegram import *
from telegram.ext import *
import MainBot

APIKey = "1607299983:AAHPq93CT_V3wx6NZKduwSgrI4dEWhSrlUs"
MyBot = Bot(APIKey)

UpdateMyBot = Updater(APIKey,use_context=True)
DispatchUpToBot = UpdateMyBot.dispatcher

VerifyPassword = range(1)
def AdminAccis(update:Update,context:CallbackContext):
    MyBot.send_message(
        chat_id = update.effective_chat.id,
        text = "Ok, Enter Password"
    )
    return VerifyPassword

def AdminOwnership(update:Update,context:CallbackContext):
    password = update.message.text
    passwdFile = open("passwdFile.txt",'r')
    seepasswd = passwdFile.readline()
    if(password==seepasswd):
        MyBot.send_message(
            chat_id = update.effective_chat.id,
            text = "Hello Sir/Mam,\nGreat to see you here.. to see gides click on\n[ /Admingide ]"
        )
        AccessPass = open("SpecialControlPass.txt",'a')
        AccessPass.write("{}\n".format(update.effective_chat.id))
        AccessPass.close()

    else:
        MyBot.send_message(
            chat_id = update.effective_chat.id,
            text = "Access Denide! Sorry"
        )
    return ConversationHandler.END

def isAllow(id):
    AccessPassAllow = open("SpecialControlPass.txt",'r')
    idpass = AccessPassAllow.readlines()
    status = 0
    for i in idpass:
        i = i.replace("\n", "")
        if(str(i) == str(id)):
            status = 1
        else:
            status = 0
    if(status == 1):
        return True
    else:
        return False
    

def control(update:Update,context:CallbackContext):
    commandGiven = update.message.text
    if(commandGiven in ["bye","bubye","byeeeee","Bye","ttyl"]):
        MyBot.send_message(
            chat_id = update.effective_chat.id,
            text = "Bye bye dear... it was great to spend time with you."
        )
    if(commandGiven=="server name"):
        if(isAllow(update.effective_chat.id)):
            MyBot.send_message(
                chat_id = update.effective_chat.id,
                text = "VAIO Sony Laptop"
            )
        else:
            MyBot.send_message(
                chat_id = update.effective_chat.id,
                text = "This access are only given to Admin.So, Sorry!"
            )

def adminGide(update:Update,context:CallbackContext):
    if(isAllow(update.effective_chat.id)):
        MyBot.send_message(
            chat_id = update.effective_chat.id,
            text = MainBot.datatoRead("AdminGide.txt")
        )
    else:
        MyBot.send_message(
                chat_id = update.effective_chat.id,
                text = "This access are only given to Admin.So, Sorry!"
            )