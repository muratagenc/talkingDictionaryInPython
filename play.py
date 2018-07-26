#!/usr/bin/python3
import sys
import urllib.request, re
from playsound import playsound

def getSound(word):
	#now get the sound of it
	fileName = word + ".mp3"
	try:
		playsound("./audio/" + word[0] + "/" + fileName)
	except:
		print("audio in database")
		wordAudioURL = "https://ssl.gstatic.com/dictionary/static/sounds/oxford/" + word + "--_gb_1.mp3"
		#print(wordAudioURL)
		try:
			response = urllib.request.urlretrieve(wordAudioURL, "./data/" + fileName)
			playsound("./audio/" + word[0] + "/" + fileName)
		except:
			print("audio not on the net")
			pass



def getDefinition(word):
	try:
		with open("./descriptions/" + word[0] + "/" + word + ".txt", 'r') as fin:
			print(fin.read(), end="")

	except:	
		url="http://"+ "www" + "." + "merriam-webster" + ".com/dictionary/" #link
		url=url+wordText
		text=urllib.request.urlopen(url).read().decode('utf-8') 
		str2 = re.findall('<span><span class="intro-colon">:</span>(.+?)</span>', text)
		#print("from the net: ", str2)

		if len(str2) > 0:
			file = open("./descriptions/" + word[0] + "/" + word + ".txt", 'w+')
			
			str1 = ''.join(str2)
			print(str1)
			file.write(str1)
			file.close()




##main program
print("This program requires internet connection. Type your word and hit enter")
print("by Murat Genc. mgenc@pace.edu")

while(True):
	#read the word
	wordText = input(">")
	if(wordText == "q"):
		break
	
	getDefinition(wordText)	
	getSound(wordText)

print("bye!")



