#!/usr/bin/env python

########################################################################
## reads various weather sensors and sends them to wunderground and a
## custom database
##
## * name: the title - UID for thsi measurement
## * value: the reading
## * unit: what we are measuring 
##
## CREATED: 2017/07/16 19:04:12
## MODIFIED: see https://github.com/dirtchild/weatherPi
##

########################################################################
# imports
from MODULES import weatherSensors, utilities
from config import *
import time

########################################################################
# config is all in config.py

########################################################################
# MAIN

# fire off our time-dependent sensors (wind speed, rainfall etc)
rain = ""
w.spd = ""

# loop forever. could have used threads, too big of a hammer for the job
while True:
	# read in all of our single check sensors
	w.dir = ""
	uv = ""
	temp = ""
	humid = ""
	pressure = ""

	if WEATHER_UPLOAD == True:
		# write to wunderground

		# write to our database
	else:
		print "Not sending data to online services"
		
	# log something
	print logFile

	# do something extra every N seconds - gusts, rain??? is this needed

	time.sleep(readInterval)