#!/usr/bin/python3
import os
import sys
import fileinput

textToSearch = '<span class="intro-colon">:'
textToReplace = ""

fileList = []
for dirpath, dirs, files in os.walk("./descriptions/"):
	fileList = fileList + files

for fileName in fileList:
	f = open("./descriptions/" + fileName[0] + "/" + fileName, 'r')
	fileData = f.read()
	f.close()

	newData = fileData.replace(textToSearch, textToReplace)
	f = open("./descriptions/" + fileName[0] + "/" + fileName, 'w')
	f.write(newData)
	f.close()

