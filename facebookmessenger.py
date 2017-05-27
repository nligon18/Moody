import fbchat
# Logon to Facebook
client = fbchat.Client("moodybotchat@gmail.com", "moodybotchatstuyhacks")
# Message
# Retrieve Friends List


def setContact(contactName):
	global friend
	global friends
	friends = client.getUsers(contactName)
	# print filter(lambda x: 'Matthew Cen' in x, friends)
	# friendListIndex = friends.index(contactName)
	print friends
	# Select Friend to Talk To
	friend = friends[0]
setContact('Matthew Cen')	
# Retrieve User Response
# Send User Response
messageSend = "Hello Y"
def sendMsg(messageSend):
	sent = client.send(friend.uid, messageSend)
	if sent:
	    print("Message sent successfully!")
sendMsg(messageSend)

# Retrieve Message Function
def retrieveMsg(): 
	last_messages = client.getThreadInfo(friend.uid, last_n=2)
	last_messages.reverse()  # messages come in reversed order
	for message in last_messages:
		# userResponse = [message.body]
		print(len(message.body[1]))
		# return message.body
retrieveMsg()
