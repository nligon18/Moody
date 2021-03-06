import MoodyBot

LETTERS="abcdefghijklmnopqrstuvwxyz"
SYMBOLS="!@#$%^&*();:.><,/|{}'~`[]{}'"
NUMBERS="123456789"
ENDS=["bye","goodbye","adios","see ya","see you later","good bye"]
WORDS_BEFORE_NAMES=["is","named","am","im"]
PRONOUN_MAPS={"you":"i","i":"you","we":"you guys","he":"he","she":"she","they":"they","us":"you guys","me":"you","it":"it","am":"are","im":"you are","my":"your","your":"my","mine":"yours","yours":"mine","ours":"yours"}
PRONOUNS=["you","i","we","they","it","he","she","me","us","am","are","im","your","my","mine","yours"]

def findName(name):
    words=name.split(" ")
    for i in range(0,len(words)-1):
        if words[i] in WORDS_BEFORE_NAMES:
            return words[i+1]
    return name

def findQuestion(message,end):
    

def botResponse(message,mood):
    if mood=="Joy":
        mood="happy"
    if mood=="Anger":
        mood="angry"
    if mood=="Disgust":
        mood+="ed"
    if mood=="Sadness":
        mood="sad"
    if mood=="Fear":
        mood="scared"
    response=""
    end=message.find("?")
    if end!=-1:
        question=findQuestion(message,end)
        
    elif message[0]=="i":
        words=message.split(" ")
        for i in range(0,len(words)):
            if words[i] in PRONOUNS:
                words[i]=PRONOUN_MAPS[words[i]]
            response+=words[i]+" "
    else:
        response="you are "+message
    return "I understand that "+response+". Why? Are you feeling "+mood+"?"

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
    name=raw_input("Hi! My name is Moody. What is your name?\n").lower()
    name=removeUnwantedSymbols(name)
    name=removeUnwantedNumbers(name)
    name=findName(name)
    message=raw_input("Hi "+name+"! How are you?\n").lower()
    message=removeUnwantedSymbols(message)
    mood=MoodyBot.getEmotion(message)
    while not removeUnwantedNumbers(message) in ENDS:
        response=botResponse(message,mood)
        message=raw_input(response+"\n").lower()
        message=removeUnwantedSymbols(message)
        mood=MoodyBot.getEmotion(message)
    print("Bye! Come back soon!")

main()
