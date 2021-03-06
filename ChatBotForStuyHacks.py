import MoodyBot

LETTERS="abcdefghijklmnopqrstuvwxyz"
SYMBOLS="!@#$%^&*();:.><,/?|{}'~`[]{}'"
NUMBERS="123456789"
ENDS=["bye","goodbye","adios","see ya","see you later","good bye"]
WORDS_BEFORE_NAMES=["is","named","am","im"]
PRONOUN_MAPS={"you":"i","i":"you","we":"you guys","he":"he","she":"she","they":"they","us":"you guys","me":"you","it":"it","am":"are","im":"you are","my":"your","your":"my","mine":"yours","yours":"mine","ours":"yours"}
PRONOUNS=["you","i","we","they","it","he","she","me","us","am","are","im","your","my","mine","yours"]
BAD_KEY_WORDS=['terrible','awful','bad','horrible']
GOOD_KEY_WORDS=['good','great','amazing','spectacular','awesome','fantastic']
GREETINGS=["hi","hey","hello","sup","hola"]


def findName(name):
    words=name.split(" ")
    for i in range(0,len(words)-1):
        if words[i] in WORDS_BEFORE_NAMES:
            return words[i+1]
    return name

#def findQuestion(message, end):

def modifyMood(mood):
    if mood=="Joy":
        return "happy"
    if mood=="Anger":
        return "angry"
    if mood=="Disgust":
        return "disgusted"
    if mood=="Sadness":
        return "sad"
    if mood=="Fear":
        return "scared"
    return mood

def changePronouns(message):
    response=""
    words=message.split(" ")
    for i in range(0,len(words)):
        if words[i] in PRONOUNS:
            words[i]=PRONOUN_MAPS[words[i]]
        response+=words[i]+" "
    return response[:-1]

def checkForWord(message,word):
    words=message.split(" ")
    for item in words:
        if item==word:
            return True
    return False

def checkForWords(message,words):
    words=message.split(" ")
    for word in words:
        if word in GREETINGS:
            return True
    return False

def botResponse(message,mood,lastMood,questionAsked,whatAskedAbout):
    #print("last mood is "+lastMood)
    #print(message)
    #print("what asked about in the bot response is "+whatAskedAbout)
    sameMood= (mood==lastMood)
    mood=modifyMood(mood)                                                           #Finds Mood
    response=""
    #end=message.find("?")
    #if end!=-1:
    #    question=findQuestion(message,end)#finds what the question is
    if checkForWords(message,GREETINGS):
        return ("Hi! My name is Moody. What is your name?",True,"name")
    response=changePronouns(message)
    if questionAsked==True:
       # print("question was asked")
        if whatAskedAbout=="mood":
            #print("question was about mood")
            if checkForWord(message,"yes")==True:
                if lastMood=="happy":
                    whatAskedAbout="why happy"
                    return ("I am glad you are happy! Why are you happy?",questionAsked,whatAskedAbout)
                else:
                    whatAskedAbout="why "+lastMood
                    return ("Oh, I am sorry you are "+lastMood+". I hope you feel better soon. Why do you feel "+lastMood+"?",questionAsked,whatAskedAbout)
            return ("I'm sorry.",False,"none")
        
        if whatAskedAbout=="name":
            #print("question was about name")
            name=findName(message)
            questionAsked=True
            whatAskedAbout="day"
            return ("Hi "+name+"! How was your day?",questionAsked,whatAskedAbout)

        if whatAskedAbout=="day":
            if checkForWords(message,GOOD_KEY_WORDS):
                return ("It sounds like you had a good day!",False,"none")
            if checkForWords(message,BAD_KEY_WORDS):
                return ("It sounds like you had a bad day. I am sorry.",False,"none")
            
    if not message[0]=="i":
        response="you are "+message
    if mood=="unsure":
        questionAsked=True
        whatAskedAbout="day"
        return ("Oh, "+response+". How was your day?",questionAsked,whatAskedAbout)                             #two responses
    if sameMood:
        questionAsked=False
        finalResponse="Oh, "+response+"."
    else:
        questionAsked=True
        whatAskedAbout="mood"
        finalResponse="Oh, "+response+". Are you feeling "+mood+"?"
    return (finalResponse,questionAsked,whatAskedAbout)


def removeUnwantedNumbers(message):
    for item in NUMBERS:
        parts=message.split(item)
        message=""
        for part in parts:
            message=message+part
    return message

def removeUnwantedSymbols(message):
    for item in SYMBOLS:
        parts=message.split(item)
        message=""
        for part in parts:
            message=message+part
    return message

def main():
    lastMood="unsure"
    questionAsked=False
    whatAskedAbout="none"
    
    name=raw_input("Hi! My name is Moody. What is your name?\n").lower()
    name=removeUnwantedSymbols(name)
    name=removeUnwantedNumbers(name)
    name=findName(name)

    
    message=raw_input("Hi "+name+"! How are you?\n").lower()
    message=removeUnwantedSymbols(message)


    while not removeUnwantedNumbers(message) in ENDS:
        mood=modifyMood(MoodyBot.getEmotion(message))

        
        response,questionAsked,whatAskedAbout=botResponse(message,mood,lastMood,questionAsked,whatAskedAbout)


        lastMood=mood

        
        message=raw_input(response+"\n").lower()
        message=removeUnwantedSymbols(message)

        
        mood=MoodyBot.getEmotion(message)

        
    print("Bye! Come back soon!")

#main()
