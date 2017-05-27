# Imports
import json
import requests
from watson_developer_cloud import *

# Credentials
tone_analyzer = ToneAnalyzerV3(
  username='4e64dd0c-dd6a-43c5-87af-7693c400e0fb',
  password='6u2MsruCAn6k',
  version='2016-05-19'
)
# Function
def getEmotion(user_response):
	user_response = json.dumps(user_response)
	# User JSON
	#with open('text.json') as f:
	#	tone = tone_analyzer.tone(json.load(f)['text'], tones='emotion')
	#	response = json.dumps(tone, indent=2)
	#	print response
	# User Text String Input
	tone = tone_analyzer.tone(user_response, tones='emotion')
	response = json.dumps(tone, indent=2)
	#print response


	responseSelector = json.loads(response)
	# print responseSelector['document_tone']['tone_categories'][0]['tones'][indexcount]['score']
	responseArray = []
	indexvalue = 6
	# Loop to place all emotion values into list
	for indexvalue in xrange(0,5):
		responseArray.append(responseSelector['document_tone']['tone_categories'][0]['tones'][indexvalue]['score'])
		indexvalue - 1
	# Determines most likely emotion and its value + key
	emotionKeyIndex = responseArray.index(max(responseArray))
	emotionValue = responseSelector['document_tone']['tone_categories'][0]['tones'][emotionKeyIndex]['tone_name']
	#print emotionValue
	return emotionValue
	# loop 5 times place values into python array
