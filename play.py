#!/usr/bin/python3
import sys
import urllib.request, re
from playsound import playsound

print("This program requires internet connection. Type your word and hit enter")
print("by Murat Genc. mgenc@pace.edu")

while(True):
	#read the word
	wordText = input(">")
	if(wordText == "q"):
		break
	try:	
		#to get description of the word
		url="http://"+ "www" + "." + "merriam-webster" + ".com/dictionary/" #link
		#url = "http://www.dictionary.com/cgi-bin/dict.pl?term=%s" % wordText
		url=url+wordText
		text=urllib.request.urlopen(url).read().decode('utf-8') #open the url, read it and change the encoding to utf-8. Needed to use regex on it
		print(re.findall('<meta name="description" content="(.+?)">', text))
		print(re.findall('<span><span class="intro-colon">:</span>(.+?)</span>', text))

		#print(re.findall('<span><span class="intro-colon">:</span>(.+?)</span>', text)) #regex finds all occurences of the specific
	except:
		pass
	

	#now get the sound of it
	fileName = wordText + ".mp3"
	try:
		playsound("./data/" + fileName)
	except:
		print("not in database")
		wordAudioURL = "https://ssl.gstatic.com/dictionary/static/sounds/oxford/" + wordText + "--_gb_1.mp3"
		#print(wordAudioURL)
		try:
			response = urllib.request.urlretrieve(wordAudioURL, "./data/" + fileName)
			playsound("./data/" + fileName)
		except:
			print("not on the net")
			pass

