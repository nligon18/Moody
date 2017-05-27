import fbchat
# Logon to Facebook
client = fbchat.Client("moodybotchat@gmail.com", "moodybotchatstuyhacks")
# Message
# message = "I'm happy"
# Retrieve Friends List
friends = client.getUsers("FRIEND'S NAME")
print friends
# Select Friend to Talk To

# Retrieve User Response
# def rtrMsg():
	
# Send User Response
def sendMsg():
	sent = client.send(friend.uid, message)
	if sent:
	    print("Message sent successfully!")