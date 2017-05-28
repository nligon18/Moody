import fbchat
import requests
import json

def  getName(author_id):
	url = "https://graph.facebook.com/" + author_id + "?fields=name&access_token=1910943402516729|NFxHu_FCpNW-Cj1zHRIIfoB5FQI"
	FBresponse = requests.get(url)
	parsed_json = json.loads(FBresponse.text)
	print parsed_json["name"]
	return parsed_json["name"]
# # Logon to Facebook
# client = fbchat.Client("moodybotchat@gmail.com", "moodybotchatstuyhacks")
# # Message
# # Retrieve Friends List

#
# def setContact():
# 	global friend
# 	global friends
# 	friends = client.getUsers(contactName)
# 	# print filter(lambda x: 'Matthew Cen' in x, friends)
# 	# indices = [i for i, s in enumerate(friends) if contactName in s]
# 	# print indices
# 	# friendListIndex = friends.index(contactName)
# 	print friends
# 	# Select Friend to Talk To
# 	friend = friends[0]	

# # Send User Response
# messageSend = "Hello I'm moody bot"
# def sendMsg(messageSend):
# 	sent = client.send(friend.uid, messageSend)
# 	if sent:
# 	    print("Message sent successfully!")
# sendMsg(messageSend)

# Retrieve Message Function
def retrieveMsg(): 
	last_messages = client.getThreadInfo(author_id, last_n=2)
	last_messages.reverse()  # messages come in reversed order
	for message in last_messages:
		# userResponse = [message.body]
		print(message.body)
		# return message.body

class EchoBot(fbchat.Client):

    def __init__(self,email, password, debug=True, user_agent=None):
        fbchat.Client.__init__(self,email, password, debug, user_agent)

    def on_message(self, mid, author_id, author_name, message, metadata):
        self.markAsDelivered(author_id, mid) #mark delivered
        self.markAsRead(author_id) #mark read
        
        moodyResponse = BotResponse(getName(author_id))
        # if you are not the author, echo
        if str(author_id) != str(self.uid):
            self.send(author_id,moodyResponse)

bot = EchoBot("moodybotchat@gmail.com", "moodybotchatstuyhacks")
bot.listen()
