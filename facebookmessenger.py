import fbchat
# Logon to Facebook
client = fbchat.Client("moodybotchat@gmail.com", "moodybotchatstuyhacks")
# Message
# message = "I'm happy"
# Retrieve Friends List
friends = client.getUsers("Matthew Cen")
print friends
# Select Friend to Talk To
friend = friends[0]
# Retrieve User Response

# Send User Response
def sendMsg(messageSend):
	sent = client.send(friend.uid, messageSend)
	if sent:
	    print("Message sent successfully!")
# sendMsg(messageSend)

# Retrieve Message Function
def retrieveMsg(): 
	last_messages = client.getThreadInfo(friend.uid, last_n=1)
	last_messages.reverse()  # messages come in reversed order
	for message in last_messages:
		# userResponse = [message.body]
		print(message.body)
		# return message.body
retrieveMsg()
