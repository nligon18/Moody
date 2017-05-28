import fbchat
import requests
import json
import ChatBotForStuyHacks as cb
import MoodyBot

def  getName(author_id):
	url = "https://graph.facebook.com/" + author_id + "?fields=name&access_token=1910943402516729|NFxHu_FCpNW-Cj1zHRIIfoB5FQI"
	FBresponse = requests.get(url)
	parsed_json = json.loads(FBresponse.text)
	print parsed_json["name"]
	return parsed_json["name"]
 # # Logon to Facebook
client = fbchat.Client("moodybotchat@gmail.com", "moodybotchatstuyhacks")
# client = fbchat.Client("moodybotchat@gmail.com", "moodybotchatstuyhacks")
 # # Message
 # # Retrieve Friends List
 

def setContact():
	global friend
	global friends
	friends = client.getUsers(contactName)
	# print filter(lambda x: 'Matthew Cen' in x, friends)
	# indices = [i for i, s in enumerate(friends) if contactName in s]
	# print indices
	# friendListIndex = friends.index(contactName)
	
 
 # # Send User Response
 # messageSend = "Hello I'm moody bot"
class EchoBot(fbchat.Client):
     def on_message(self, mid, author_id, author_name, message, metadata):
         self.markAsDelivered(author_id, mid) #mark delivered
         self.markAsRead(author_id) #mark read
         lastMood="unsure"
         questionAsked=False
         whatAskedAbout="none"
         message = cb.removeUnwantedSymbols(message)
         mood = MoodyBot.getEmotion(message)
         moodyResponse = cb.botResponse(message, mood, lastMood, questionAsked, whatAskedAbout)

         # if you are not the author, echo
         if str(author_id) != str(self.uid):
            self.send(author_id,author_id)
            self.send(author_id,moodyResponse)
 
bot = EchoBot("moodybotchat@gmail.com", "moodybotchatstuyhacks")
bot.listen()
