from telegram import *
from telegram.ext import *
import random
import json
import AdminBot

APIKey = "1607299983:AAHPq93CT_V3wx6NZKduwSgrI4dEWhSrlUs"
MyBot = Bot(APIKey)

UpdateMyBot = Updater(APIKey,use_context=True)
DispatchUpToBot = UpdateMyBot.dispatcher

def datatoRead(filename):
    filename = open(filename,'r')
    see = filename.readlines()
    data = ""
    for i in see:
        data = data + i
    return data

def SayingThought(update:Update,context:CallbackContext):
    thoughtsfile = open("thoughts.txt",'r')
    takethoughts = thoughtsfile.readlines()
    pickAnyOne = random.randint(0,len(takethoughts))
    MyBot.send_message(
        chat_id = update.effective_chat.id,
        text = takethoughts[pickAnyOne]
    )

def StartChatting(update:Update,context:CallbackContext):
    MyBot.send_message(
        chat_id = update.effective_chat.id,
        text = datatoRead("startgide.txt")
    )
    if(update.effective_chat.id not in AdminBot.userIDlist()):
        userIDdetails = open("botData.json",'r')
        dataLoadofusers = json.load(userIDdetails)
        userIDdetails.close()
        adduserID = open("botData.json",'w')
        dataLoadofusers["users"].append(update.effective_chat.id)
        json.dump(dataLoadofusers,adduserID,indent=4)
        adduserID.close()


def TheNewthings(update:Update,context:CallbackContext):
    MyBot.send_message(
        chat_id = update.effective_chat.id,
        text = datatoRead("whatsnew.txt")
    )

sendingfeed = range(1)
def UserFeedBack(update:Update,context:CallbackContext):
    MyBot.send_message(
        chat_id = update.effective_chat.id,
        text = "That's great your feedback is really have a huge value for us.. So, Start typing your feedback :"
    )
    return sendingfeed
def TQforfeeds(update:Update,context:CallbackContext):    
    MyBot.send_message(
        chat_id = update.effective_chat.id,
        text = "FeedBack Page Close"
    )   
    return ConversationHandler.END
def feedbacktyper(update:Update,context:CallbackContext):
    thefeedback = update.message.text
    FeedBackfile = open('FeedBackPage.txt','a')
    data = '\nUserID{}: Feedback is :- {}'.format(update.effective_chat.id,thefeedback)
    FeedBackfile.write(data)       
    FeedBackfile.close()

    MyBot.send_message(
        chat_id = update.effective_chat.id,
        text = "ThankYou for your feedback..."
    )  
    return ConversationHandler.END

EchoChat,EchoSticker = range(2)
def startingEcho(update:Update,context:CallbackContext):
    MyBot.send_message(
        chat_id = update.effective_chat.id,
        text = "Starting the Echo.\n[For stoping echo: /stopecho]"
    )
    return EchoChat,EchoSticker
def echoTheText(update:Update,context:CallbackContext):
    MyBot.send_message(
        chat_id = update.effective_chat.id,
        text = update.message.text
    )
def echoTheSticker(update:Update,context:CallbackContext):
    MyBot.send_sticker(
        chat_id = update.effective_chat.id,
        sticker = update.message.sticker.file_id
    )
def stopingEcho(update:Update,context:CallbackContext):
    MyBot.send_message(
        chat_id = update.effective_chat.id,
        text = "Echo is stoped now"
    )
    return ConversationHandler.END

def mainControl():
    StartChat = CommandHandler("start",StartChatting)
    WhatsNew = CommandHandler(["whatsnew","help"],TheNewthings)
    AdminGide = CommandHandler("admingide",AdminBot.adminGide)
    FeedBack = ConversationHandler(
        entry_points=[CommandHandler("feedback",UserFeedBack)],
        states={sendingfeed:[MessageHandler(Filters.text,feedbacktyper)]},
        fallbacks=[CommandHandler("sendfeed",TQforfeeds),MessageHandler(Filters.text,feedbacktyper)]
    )
    Thought = CommandHandler(["saythought","quote"],SayingThought)
    EchoState = ConversationHandler(
        entry_points=[CommandHandler(["startecho"],startingEcho)],
        states={
            EchoChat:[MessageHandler(Filters.text,echoTheText)],
            EchoSticker:[MessageHandler(Filters.sticker,echoTheSticker)]
        },
        fallbacks=[
            CommandHandler(["stopecho"],stopingEcho),
            MessageHandler(Filters.text,echoTheText),
            MessageHandler(Filters.sticker,echoTheSticker)
        ]
    )
    AdminPass = ConversationHandler(
        entry_points=[CommandHandler(["admin"],AdminBot.AdminAccis)],
        states={
            AdminBot.VerifyPassword:[MessageHandler(Filters.text,AdminBot.AdminOwnership)]
        },
        fallbacks=[MessageHandler(Filters.text,AdminBot.AdminOwnership)]
    )
    NoticeSender = ConversationHandler(
        entry_points=[CommandHandler(["notice"],AdminBot.notice)],
        states={
            AdminBot.sendnoticetousers:[MessageHandler(Filters.text,AdminBot.sendnotice)]
        },
        fallbacks=[MessageHandler(Filters.text,AdminBot.sendnotice)]
    )
    UsersLocation = ConversationHandler(
        entry_points=[CommandHandler(["weather"],AdminBot.askingWeather)],
        states={
            AdminBot.seeLocation:[MessageHandler(Filters.location,AdminBot.weatherReport)]
        },
        fallbacks=[MessageHandler(Filters.location,AdminBot.weatherReport)]
    )
    Admincontrol = MessageHandler(Filters.text,AdminBot.control)

    DispatchUpToBot.add_handler(AdminPass)
    DispatchUpToBot.add_handler(NoticeSender)
    DispatchUpToBot.add_handler(StartChat)
    DispatchUpToBot.add_handler(AdminGide)
    DispatchUpToBot.add_handler(UsersLocation)
    DispatchUpToBot.add_handler(WhatsNew)
    DispatchUpToBot.add_handler(FeedBack)
    DispatchUpToBot.add_handler(Thought)
    DispatchUpToBot.add_handler(EchoState)
    DispatchUpToBot.add_handler(Admincontrol)

    UpdateMyBot.start_polling()

if __name__ == "__main__":
    mainControl()
    
