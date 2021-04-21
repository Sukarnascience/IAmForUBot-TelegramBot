from datetime import datetime
from datetime import date
import json
import requests 

OpenMapAPIKey = "<--- OpenMapAPI Key --->"

def commandsGiven(userSay):
    data = userSay.split()
    if("what" in data or "what's" in data):
        if("name" in data):
            return "I don't have any specific name but my other friends call me as 'IAmForU bot'"
        elif("time" in data):
            today = datetime.now()
            return "So, in my place accoring to my clock its {} IST".format(today.strftime("%H:%M:%S"))
        elif("date" in data):
            today = date.today()
            return "So, According to my place, today's date is: {}".format(today.strftime("%B %d, %Y"))
        elif("meaning" in data or "mean" in data):
            scarchword = None
            for i in data:
                if(i not in ["what","is","the","meaning","of","do","we","mean","by","?",".","!",":","say","to","you","can","me"]):
                    scarchword = i
            if(scarchword!=None):
                dictionaryBook = open("dictionary.json",'r')
                dictionaryData = json.load(dictionaryBook)
                dictionaryBook.close()
                if(scarchword in list(dictionaryData.keys())):
                    return "The meaning of the word '{}' is : {}".format(scarchword,dictionaryData[scarchword])
                else:
                    return "Sorry, I don't know the meaning of '{}'.".format(i)
            else:
                return None
        else:
            return None
    else:
        return None

def aiReply(userSay):
    reply = "AI is still not developed properly"
    return reply

def weather(lon,lat):
    sendDatatoUser = ""
    callUrl=("http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}").format(lat,lon,OpenMapAPIKey)
    dataIn = requests.get(callUrl)
    getData = dataIn.json()

    sendDatatoUser = sendDatatoUser + "Weather Report of {} area is:".format(getData['name'])
    sendDatatoUser = sendDatatoUser + "\n\nDiscription :{}".format(getData['weather'][0]['description'])
    sendDatatoUser = sendDatatoUser + "\nTemperature :{}{}C".format(int(int(getData['main']['temp'])- 273.15),chr(176))
    sendDatatoUser = sendDatatoUser + "\nMax. Temp.:{}{}C".format(int(int(getData['main']['temp_max'])- 273.15),chr(176))
    sendDatatoUser = sendDatatoUser + "\nMin. Temp.:{}{}C".format(int(int(getData['main']['temp_min'])- 273.15),chr(176))
    sendDatatoUser = sendDatatoUser + "\nYou will feel like :{}{}C".format(int(int(getData['main']['feels_like'])- 273.15),chr(176))
    sendDatatoUser = sendDatatoUser + "\nHumidity :{}%".format(int(getData['main']['humidity']))
    
    return sendDatatoUser
