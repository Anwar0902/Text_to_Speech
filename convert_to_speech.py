#!/usr/bin/env python
import pyttsx3
import os 
engine = pyttsx3.init()
file = open("_tweets.txt",'r')
lines = file.readlines()
file.close()
for line in lines :
	line = "the date is " + line
	print (line)
	rate = engine.getProperty('rate')
	engine.setProperty('rate',rate-10)
	engine.say(line)
engine.runAndWait()
