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
w_spd = ""

# loop forever. could have used threads, too big of a hammer for the job
while True:
	# read in all of our single check sensors
	w_dir = ""
	uv = ""
	temp = ""
	humid = ""
	pressure = ""

	# work out our dew point
	print "[DEBUG]	i'm a dew point"

	if WEATHER_UPLOAD == True:
		#DEBUG
		print "[DEBUG]	writing stuff to online stuff"
		# write to wunderground

		# write to our database
	else:
		print "[DEBUG]	Not sending data to online services"
		
	# log something?
	print logFile
	time.sleep(readInterval)