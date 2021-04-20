from telegram import *
from telegram.ext import *
import MainBot
import random
import json

APIKey = "<---- bot key ---->"
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
    passwdFile = open("botData.json",'r')
    dataFetched = json.load(passwdFile) 
    seepasswd = dataFetched['password']
    passwdFile.close()
    if(password.lower()==seepasswd):
        MyBot.send_message(
            chat_id = update.effective_chat.id,
            text = "Hello Sir/Mam,\nGreat to see you here.. to see gides click on\n[ /Admingide ]"
        )
        CAccessPass = open("botData.json",'r')
        CeditAccessdata = json.load(CAccessPass)
        CAccessPass.close()
        if(int(update.effective_chat.id) not in CeditAccessdata["admin"]):
            AccessPass = open("botData.json",'w')
            CeditAccessdata["admin"].append(int(update.effective_chat.id))
            json.dump(CeditAccessdata,AccessPass,indent=4)
            AccessPass.close()

    else:
        MyBot.send_message(
            chat_id = update.effective_chat.id,
            text = "Access Denide! Sorry"
        )
    return ConversationHandler.END

def userIDlist():
    ID = open("botData.json",'r')
    dataFetchedID = json.load(ID)
    IDList = dataFetchedID["users"]
    ID.close()
    return IDList

def isAllow(id):
    AccessPassAllow = open("botData.json",'r')
    idpass = json.load(AccessPassAllow)
    status = 0
    adminList = idpass["admin"]
    if(id in adminList):
        status = 1
    else:
        status = 0
    AccessPassAllow.close()
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
    if(commandGiven.lower()=="server name"):
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
    if(commandGiven.lower()=="total users"):
        if(isAllow(update.effective_chat.id)):
            see_noOfusers = open("botData.json",'r')
            totalUsers = json.load(see_noOfusers)
            MyBot.send_message(
                chat_id = update.effective_chat.id,
                text = "Total {} users are using this bot now.".format(len(totalUsers["users"]))
            )
            see_noOfusers.close()
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
