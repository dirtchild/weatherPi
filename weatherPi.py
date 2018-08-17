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
from __future__ import print_function
from config import *
from datetime import datetime
from urllib import urlencode
from weatherSensors import convertors,DHT11,eventSensor,MPL3115A2,SensorData,uv,windDirection
import MySQLdb as my
import time
import sys
import urllib2
import requests

# fire off our time-dependent sensors (wind speed, rainfall etc)
wSpeed = eventSensor.eventSensor(W_SPD_GPIO, W_SPD_CALIBRATION, "wind speed events", "w_spd", "MPH", W_SPD_EVENTS_PERIOD)
rain = eventSensor.eventSensor(RAIN_GPIO, RAIN_CALIBRATION, "rain events", "rain", "mm", RAIN_EVENTS_PERIOD)

# loop forever.
while True:
	# read in all of our single check sensors for this run
	dhtTem,dhtHum = DHT11.getReading()
	mplTem,mplPres,mplAlt = MPL3115A2.getReading()
	UV,solarradiation = uv.getReading()
	windDir = windDirection.getReading()
	windSpeedNow = wSpeed.getPeriodAverage("windSpeedNow",readInterval)
	windSpdMph_avg2m = wSpeed.getPeriodAverage("windSpdMph_avg2m",120)
	rainIn = rain.getPeriodTotal("rainIn", readInterval)
	dailyrainin = convertors.mmToInches(rain.getPeriodTotal("dailyrainin", 86400).value)

	# setup our reading variables to make things better for human brains
	# and to amke the rest of this easier
	tempf = (mplTem.value + dhtTem.value) / 2 # average both internal temp readings
	winddir = windDir.value
	windspeedmph = windSpeedNow.value
	windgustmph = "0"
	windgustdir = "0"
	windspdmph_avg2m = windSpdMph_avg2m.value
	winddir_avg2m = "0"
	windgustmph_10m = "0"
	windgustdir_10m = "0"
	humidity = dhtHum.value
	dewptf = convertors.dewpointF(tempf, dhtHum.value)
	rainin = convertors.mmToInches(rainIn.value)
	baromin = mplPres.value
	weather = "0"
	clouds = "0"
	soiltempf = "0"
	soilmoisture = "0"
	leafwetness = "0"
	solarradiation = solarradiation.value
	UV = UV.value
	visibility = "0"
	indoortempf = "0"
	indoorhumidity = "0"

        sys.stdout.flush()

	# do the work
	if WUNDERGROUND_UPLOAD == True:
		# write to wunderground
		weather_data_wu = {
			"action": "updateraw",
			"ID": WU_STATION_ID,
			"PASSWORD": WU_STATION_KEY,
			"dateutc": "now",
			"winddir": str(winddir),
			"windspeedmph": str(windspeedmph),
			"windgustmph": str(windgustmph),
			"windgustdir": str(windgustdir),
			"windspdmph_avg2m": str(windspdmph_avg2m),
			"winddir_avg2m": str(winddir_avg2m),
			"windgustmph_10m": str(windgustmph_10m),
			"windgustdir_10m": str(windgustdir_10m),
			"humidity": str(humidity),
			"dewptf": str(dewptf),
			"tempf": str(tempf),
			"rainin": str(rainin),
			"dailyrainin": str(dailyrainin),
			"baromin": str(baromin),
			"weather": str(weather),
			"clouds": str(clouds),
			"soiltempf": str(soiltempf),
			"soilmoisture": str(soilmoisture),
			"leafwetness": str(leafwetness),
			"solarradiation": str(solarradiation),
			"UV": str(UV),
			"visibility": str(visibility),
			"indoortempf": str(indoortempf),
			"indoorhumidity": str(indoorhumidity)}
		try:
			upload_url = WU_URL + "?" + urlencode(weather_data_wu)
			response = urllib2.urlopen(upload_url)
			html = response.read()
			response.close()  # best practice to close the file
		except Exception, e:
			print("Wunderground Exception:", str(e))

	if WOW_UPLOAD == True:
		# write to WOW: http://wow.metoffice.gov.uk/support/dataformats#automatic
		weather_data_wow = {
			"siteid": WOW_STATION_ID,
			"siteAuthenticationKey": WOW_STATION_KEY,
			"dateutc": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
			"softwaretype": "custom",
			"winddir": str(winddir),
			"windspeedmph": str(windspeedmph),
			"windgustmph": str(windgustmph),
			"windgustdir": str(windgustdir),
			"humidity": str(humidity),
			"dewptf": str(dewptf),
			"tempf": str(tempf),
			"rainin": str(rainin),
			"dailyrainin": str(dailyrainin),
			"baromin": str(baromin)}
		try:
			upload_url = WOW_URL + "?" + urlencode(weather_data_wow)
			response = urllib2.urlopen(upload_url)
			html = response.read()
			response.close()  # best practice to close the file
		except Exception, e:
			print("WOW Exception:", str(e))

	# write to our database
	if DATABASE_UPLOAD == True:
		url_string_remote = 'http://home:8086/write?db=home_environment'
                url_string_local = 'http://127.0.0.1:8086/write?db=weather_cache'
		data_string = "external,source=weatherStation " \
				"winddir="+str(winddir)+"," \
				"windspeedmph="+str(round(windspeedmph,2))+"," \
				"windgustmph="+str(windgustmph)+"," \
				"windgustdir="+str(windgustdir)+"," \
				"hum="+str(humidity)+"," \
				"dewptf="+str(round(convertors.f_to_c(dewptf),2))+"," \
				"tem="+str(convertors.f_to_c(tempf))+"," \
				"rainin="+str(rainin)+"," \
				"dailyrainin="+str(dailyrainin)+"," \
				"baromin="+str(round(baromin,2))
		try:
                        #DEBUG
			#print(url_string, data_string)
			r = requests.post(url_string_remote, data=data_string)
                        print("weather_data_db::",url_string_remote, data_string)
		except Exception, e:
			print("DB Exception, logging locally:", str(e))
                        r = requests.post(url_string_local, data=data_string)
                        print("weather_data_db::",url_string_local, data_string)

	print("weather_data_wu::",weather_data_wu)
	print("weather_data_wow::",weather_data_wow)
	sys.stdout.flush()

	# wait on a bit
	time.sleep(readInterval)
