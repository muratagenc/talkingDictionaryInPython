#!/usr/bin/python3
import sys
import urllib.request, re
from playsound import playsound
import os
from random import randint
import time





def getSound(word):
	#now get the sound of it
	fileName = word + ".mp3"
	try:
		playsound("./audio/" + word[0] + "/" + fileName)
	except:
		print("audio not in the database")
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
		print("description not in the database")
		try:
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
		except:
			print("description not on the net")
			pass		







def getFileList():
	#fill the array with file names
	fileList = []
	for dirpath, dirs, files in os.walk("./descriptions/"):
		fileList = fileList + files

	size = len(fileList)

	#print(fileList[120][:-4])
	
	filePicked = fileList[randint(0,size)][:-4]

	try:
		with open("./descriptions/" + filePicked[0] + "/" + filePicked + ".txt", 'r') as fin:
			description = fin.read()
	except:
		description =''
		pass
	
	#print(filePicked)
	#print(description)
	arr = [filePicked, description]

	#return the word and its description text
	return arr






def wordGame():
	while(True):
	#print(getFileList())
		os.system('clear')
		item = getFileList()
		theQuestion = item[0]
		theAnswer = item[1]
		print(theQuestion)
		getSound(theQuestion)
		time.sleep(1)
		print(theAnswer)		

		#press enter to continue
		pause = input("")
		if pause:
			break





#main program
print("This program requires internet connection. Type your word and hit enter")
print("by Murat Genc. mgenc@pace.edu")

choice = input("(p)lay the game or (t)train? [t]: ")

if choice == "t" or choice == "":
	while(True):
		#read the word
		wordText = input(">")
		if(wordText == "q"):
			break
	
		getDefinition(wordText)
		print()
		getSound(wordText)
	
	print("bye!")
else:
	print("let's play!")
	wordGame()





