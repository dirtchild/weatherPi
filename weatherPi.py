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
wSpeed = eventSensor(W_SPD_GPIO, W_SPD_CALIBRATION, "wind speed events", "w_spd", "MPH", W_SPD_EVENTS_PERIOD)
rain = eventSensor(RAIN_GPIO, RAIN_CALIBRATION, "rain events", "rain", "mm", RAIN_EVENTS_PERIOD)

# loop forever.
while True:
	# read in all of our single check sensors
	dhtTem,dhtHum = weatherSensors.DHT11.getReading()
	mplTem,mplPres,mplAlt = weatherSensors.MPL3115A2.getReading()
	uv = weatherSensors.uv.getReading()
	windDir = weatherSensors.windDirection.getReading()

	# work out our dew point
	print "[DEBUG]	i'm a dew point from: https://github.com/cmcginty/PyWeather/tree/master/weather/units"

	if WEATHER_UPLOAD == True:
		#DEBUG
		print "[DEBUG]	writing stuff to online stuff"
		# write to wunderground

		# write to our database
	else:
		print "[DEBUG]	Not sending data to online services"
		
	# log something?
	print "[DEBUG] log to logFile"
	time.sleep(readInterval)