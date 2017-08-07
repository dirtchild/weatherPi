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
from weatherSensors import *
from config import *
import time


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

	# calculate a few thigns
	tempF = (mplTem + dhtTem) / 2
	dpF = dewpointF(tempF, dhtHum)

	# do the work
	if WEATHER_UPLOAD == True:
		#DEBUG
		print "[DEBUG]	writing stuff to online stuff"
		# write to wunderground

		# write to our database
	else:
		print "[DEBUG]	Not sending data to online services"
		
	# log something?
	print "[DEBUG] log to logFile"
	
	# wait on a bit
	time.sleep(readInterval)


###################################################################################
# WUNDERGROUP API REFERENCE
# 
# http://wiki.wunderground.com/index.php/PWS_-_Upload_Protocol
#
#-----FIELDS-----
# action=updateraw
# ID
# PASSWORD
# dateutc=now
# winddir - [0-360 instantaneous wind direction]
# windspeedmph - [mph instantaneous wind speed]
# windgustmph - [mph current wind gust, using software specific time period]
# windgustdir - [0-360 using software specific time period]
# windspdmph_avg2m  - [mph 2 minute average wind speed mph]
# winddir_avg2m - [0-360 2 minute average wind direction]
# windgustmph_10m - [mph past 10 minutes wind gust mph ]
# windgustdir_10m - [0-360 past 10 minutes wind gust direction]
# humidity - [% outdoor humidity 0-100%]
# dewptf- [F outdoor dewpoint F]
# tempf - [F outdoor temperature] 
#  * for extra outdoor sensors use temp2f, temp3f, and so on
# rainin - [rain inches over the past hour)] -- the accumulated rainfall in the past 60 min
# dailyrainin - [rain inches so far today in local time]
# baromin - [barometric pressure inches]
# weather - [text] -- metar style (+RA)
# clouds - [text] -- SKC, FEW, SCT, BKN, OVC
# soiltempf - [F soil temperature]
#  * for sensors 2,3,4 use soiltemp2f, soiltemp3f, and soiltemp4f
# soilmoisture - [%]
# * for sensors 2,3,4 use soilmoisture2, soilmoisture3, and soilmoisture4
# leafwetness  - [%]
# + for sensor 2 use leafwetness2
# solarradiation - [W/m^2]
# UV - [index]
# visibility - [nm visibility]
# indoortempf - [F indoor temperature F]
# indoorhumidity - [% indoor humidity 0-100]
# 
#-----EXAMPLE URI UPLOAD:-----
# https://weatherstation.wunderground.com/weatherstation/updateweatherstation.php?ID=KCASANFR5&PASSWORD=XXXXXX&dateutc=2000-01-01+10%3A32%3A35&winddir=230&windspeedmph=12&windgustmph=12&tempf=70&rainin=0&baromin=29.1&dewptf=68.2&humidity=90&weather=&clouds=&softwaretype=vws%20versionxx&action=updateraw# 