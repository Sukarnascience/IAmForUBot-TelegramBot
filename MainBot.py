from telegram import *
from telegram.ext import *
import random
import json

APIKey = "<---- here is my key ---->"
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

def userSaidbye(update:Update,context:CallbackContext):
    whatUsersaidnow = update.message.text
    if(whatUsersaidnow in ["bye","bubye","byeeeee","Bye","ttyl"]):
        MyBot.send_message(
            chat_id = update.effective_chat.id,
            text = "Bye bye dear... it was great to spend time with you."
        )

def TheNewthings(update:Update,context:CallbackContext):
    MyBot.send_message(
        chat_id = update.effective_chat.id,
        text = datatoRead("whatsnew.txt")
    )

sendingfeed = range(1)
def UserFeedBack(update:Update,context:CallbackContext):
    MyBot.send_message(
        chat_id = update.effective_chat.id,
        text = "That's great your feedback is really have a huge value for us.. So, Start typing your feedback.\n[to send feedback after writing: /sendfeed]"
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

STEP1,STEP2,STEP3,STEP4,STEP5,STEP6 = range(6)
UsernameOfBday = BdayDate = SenderName = modeUserSet = greatingMSGfromUser = None
def StartBdayProcess(update:Update,context:CallbackContext):
    MyBot.send_message(
        chat_id = update.effective_chat.id,
        text = "Ok, So, You want to wish you love once.\nWhat is the person username to whome you want to wish? eg:[@IAmForUBot]"
    )
    return STEP1
def listenUsername(update:Update,context:CallbackContext):
    global UsernameOfBday
    UsernameOfBday = update.message.text
    MyBot.send_message(
        chat_id = update.effective_chat.id,
        text = "Ok, Great So, When is the Birthday? eg:[06-03-2021]"
    )
    return STEP2
def listenBdayDate(update:Update,context:CallbackContext):
    global BdayDate
    BdayDate = update.message.text
    MyBot.send_message(
        chat_id = update.effective_chat.id,
        text = "Ok, Great So, what is your name from which the person recognize you? eg:[Rajdeep]"
    )
    return STEP3
def listensenderUsername(update:Update,context:CallbackContext):
    global SenderName
    SenderName = update.message.text
    MyBot.send_message(
        chat_id = update.effective_chat.id,
        text = "Ok, Great So, Should i create my own greatting type:[Y,yes] or you want to give your own message type:[N,no]? eg:[yes or no any one ]"
    )
    return STEP4
def listenUserintrest(update:Update,context:CallbackContext):
    global modeUserSet
    whatUserwant = update.message.text
    if(whatUserwant in ['y','Y',"yes","Yes"]):
        MyBot.send_message(
            chat_id = update.effective_chat.id,
            text = "Ok, Great So, I will create a lovely greating for your love onces."
        )
        modeUserSet = True
    elif(whatUserwant in ['n','N',"no","No"]):
        MyBot.send_message(
            chat_id = update.effective_chat.id,
            text = "Ok, Great So, Write your own lovely greating __Start__ :"
        )
        modeUserSet = False
    return STEP5
def CreatingCardDetails():
    return "still not maid"
def ifUsergreet(update:Update,context:CallbackContext):
    global greatingMSGfromUser
    if(modeUserSet == False):
        greatingMSGfromUser = update.message.text
        MyBot.send_message(
            chat_id = update.effective_chat.id,
            text = "Well Done, all task completed see the review :"
        )
    else:
        MyBot.send_message(
            chat_id = update.effective_chat.id,
            text = "Well Done, all task completed see the review :"
        )
    MyBot.send_message(
        chat_id = update.effective_chat.id,
        text = CreatingCardDetails()
    )
    MyBot.send_message(
        chat_id = update.effective_chat.id,
        text = "Are you satisfied by this message [y/n] or [yes/no]:"
    )  
    return STEP6  
def isUsersatisfied(update:Update,context:CallbackContext):
    whatusersaid = update.message.text
    if(whatusersaid in ['y','Y',"yes","Yes"]):
        MyBot.send_message(
            chat_id = update.effective_chat.id,
            text = "Greating Card is ready... Your msg will send to {} at currect time :)".format(UsernameOfBday)
        )
    else:
         MyBot.send_message(
            chat_id = update.effective_chat.id,
            text = "Greating Card canceled :( \nI am extreamly sorry that i am faild to not satisfied your needs\nWant to give any feedback from which i can improve myself [ /feedback ]"
        )
    return ConversationHandler.END  

ForHappy,Satisfied = range(2)
ForSad,Satisfied = range(2)
def iAmInHappyMode(update:Update,context:CallbackContext):
    MyBot.send_message(
        chat_id = update.effective_chat.id,
        text = "Wooow!\nThat's great share your this happear movement with me too...\nI would love to hear your words :)"
    )
    return ForHappy
def iAmInSadMode(update:Update,context:CallbackContext):
    MyBot.send_message(
        chat_id = update.effective_chat.id,
        text = "Aoooww. :( !\nWhat happened dear,\n   say me what happend ;("
    )
    return ForSad
def handlingsad(update:Update,context:CallbackContext):
    sadData = [
        "Awooow :(",
        "don't warry the things will again come on track",
        "don't feel bad dear",
        "keep a hope, every thing will get well soon",
        ";("]
    say = sadData[random.randint(0,4)]
    MyBot.send_message(
        chat_id = update.effective_chat.id,
        text = say
    )
def handlinghappy(update:Update,context:CallbackContext):
    happyData = [
        "Wooow :)",
        "that's really great",
        "lovely",
        ";)",
        "great going dear"
    ]
    say = happyData[random.randint(0,4)]
    MyBot.send_message(
        chat_id = update.effective_chat.id,
        text = say
    )
def iAmSatisfied(update:Update,context:CallbackContext):
    MyBot.send_message(
        chat_id = update.effective_chat.id,
        text = "I am glade that you shared your views with be, i hope now you are feeling relife by sharing your movement\n[ if not then please let my team kown that i can improve more by /feedback ]"
    )
    return ConversationHandler.END  

def mainControl():
    StartChat = CommandHandler("start",StartChatting)
    WhatsNew = CommandHandler(["whatsnew","help"],TheNewthings)
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
    BdayWish = ConversationHandler(
        entry_points=[CommandHandler("bdaywish",StartBdayProcess)],
        states={
            STEP1:[MessageHandler(Filters.text,listenUsername)],
            STEP2:[MessageHandler(Filters.text,listenBdayDate)],
            STEP3:[MessageHandler(Filters.text,listensenderUsername)],
            STEP4:[MessageHandler(Filters.text,listenUserintrest)],
            STEP5:[MessageHandler(Filters.text,ifUsergreet)],
            STEP6:[MessageHandler(Filters.text,isUsersatisfied)]
        },
        fallbacks=[]
    )
    FeelingToSayHappy = ConversationHandler(
        entry_points = [CommandHandler("iamhappy",iAmInHappyMode)],
        states={
            ForHappy:[MessageHandler(Filters.text,handlingsad)],
            Satisfied:[CommandHandler("satisfied",iAmSatisfied)]
        },
        fallbacks=[CommandHandler("satisfied",iAmSatisfied)]
    )
    FeelingToSaySad = ConversationHandler(
        entry_points = [CommandHandler("iamsad",iAmInSadMode)],
        states={
            ForSad:[MessageHandler(Filters.text,handlinghappy)],
            Satisfied:[CommandHandler("satisfied",iAmSatisfied)]
        },
        fallbacks=[CommandHandler("satisfied",iAmSatisfied)]
    )
    byebyeuser = MessageHandler(Filters.text,userSaidbye)

    DispatchUpToBot.add_handler(StartChat)
    DispatchUpToBot.add_handler(WhatsNew)
    DispatchUpToBot.add_handler(FeedBack)
    DispatchUpToBot.add_handler(Thought)
    DispatchUpToBot.add_handler(EchoState)
    DispatchUpToBot.add_handler(BdayWish)
    DispatchUpToBot.add_handler(byebyeuser)
    DispatchUpToBot.add_handler(FeelingToSayHappy)
    DispatchUpToBot.add_handler(FeelingToSaySad)

    UpdateMyBot.start_polling()

if __name__ == "__main__":
    mainControl()
    
