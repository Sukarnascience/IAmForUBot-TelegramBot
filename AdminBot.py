from telegram import *
from telegram.ext import *
import MainBot
import random

APIKey = "<-- User Key -->"
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

def userIDlist():
    IDList = []
    ID = open("userID.txt",'r')
    userId = ID.readlines()
    for i in userId:
        IDList.append(str(i.replace("\n", "")))
    return IDList

def isAllow(id):
    AccessPassAllow = open("SpecialControlPass.txt",'r')
    idpass = AccessPassAllow.readlines()
    status = 0
    adminList = []
    for i in idpass:
        adminList.append(str(i.replace("\n", "")))
    if(str(id) in adminList):
        status = 1
    else:
        status = 0
    if(status == 1):
        return True
    else:
        return False
    

def control(update:Update,context:CallbackContext):
    commandGiven = update.message.text
    commandGiven.lower()
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
sendnoticetousers = range(1)
def notice(update:Update,context:CallbackContext):
    if(isAllow(update.effective_chat.id)):
        MyBot.send_message(
            chat_id = update.effective_chat.id,
            text = "So, what is the message that you want to sent to all users..."
        )
        return sendnoticetousers
    else:
        MyBot.send_message(
                chat_id = update.effective_chat.id,
                text = "This access are only given to Admin.So, Sorry!"
            )
        return ConversationHandler.END

def sendnotice(update:Update,context:CallbackContext):
    noticeis = update.message.text
    for i in userIDlist():
        if(i!=""):
            MyBot.send_message(
                    chat_id = int(i),
                    text = noticeis
                )
    MyBot.send_message(
        chat_id = update.effective_chat.id,
        text = "noticed has been send to everyone.."
    )
    return ConversationHandler.END
