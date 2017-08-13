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

# fire off our time-dependent sensors (wind speed, rainfall etc)
wSpeed = eventSensor.eventSensor(W_SPD_GPIO, W_SPD_CALIBRATION, "wind speed events", "w_spd", "MPH", W_SPD_EVENTS_PERIOD)
rain = eventSensor.eventSensor(RAIN_GPIO, RAIN_CALIBRATION, "rain events", "rain", "mm", RAIN_EVENTS_PERIOD)

# loop forever.
while True:
	# read in all of our single check sensors for thsi run
	dhtTem,dhtHum = DHT11.getReading()
	mplTem,mplPres,mplAlt = MPL3115A2.getReading()
	UV,solarradiation = uv.getReading()
	windDir = windDirection.getReading()
	windSpeedNow = wSpeed.getPeriodAverage("windSpeedNow",30)
	windSpdMph_avg2m = wSpeed.getPeriodAverage("windSpdMph_avg2m",120)
	rainIn = rain.getPeriodTotal("rainIn", 3600)
	dailyrainin = convertors.mmToInches(rain.getPeriodTotal("dailyrainin", 86400).value)

	# setup our reading variables to make things better for human brains
	# and to amke the rest of this easier
	tempf = (mplTem.value + dhtTem.value) / 2 # average both internal temp readings
	winddir = windDir.value
	windspeedmph = windSpeedNow.value
	windgustmph = "Null"
	windgustdir = "Null"
	windspdmph_avg2m = windSpdMph_avg2m.value
	winddir_avg2m = "Null"
	windgustmph_10m = "Null"
	windgustdir_10m = "Null"
	humidity = dhtHum.value
	dewptf = convertors.dewpointF(tempf, dhtHum.value)
	rainin = convertors.mmToInches(rainIn.value)
	baromin = mplPres.value
	weather = "Null"
	clouds = "Null"
	soiltempf = "Null"
	soilmoisture = "Null"
	leafwetness = "Null"
	solarradiation = solarradiation.value
	UV = UV.value
	visibility = "Null"
	indoortempf = "Null"
	indoorhumidity = "Null"

        sys.stdout.flush()

	# do the work
	if WUNDERGROUND_UPLOAD == True:
		# write to wunderground
		weather_data = {
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
			upload_url = WU_URL + "?" + urlencode(weather_data)
			response = urllib2.urlopen(upload_url)
			html = response.read()
			#print("Server response:", html)
			response.close()  # best practice to close the file
		except Exception, e:
			print("Wunderground Exception:", str(e)) 

	# write to our database
	if DATABASE_UPLOAD == True:
		try:
			# DB connection
			db = my.connect(host=db_host,user=db_user,passwd=db_pwd,db=db_db)
			dbCursor = db.cursor()
			#DEBUG:  %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %s
			sql = "insert into %s VALUES(Null, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)" % \
				(db_table,\
				winddir,\
				windspeedmph,\
				windgustmph,\
				windgustdir,\
				windspdmph_avg2m,\
				winddir_avg2m,\
				windgustmph_10m,\
				windgustdir_10m,\
				humidity,\
				dewptf,\
				tempf,\
				rainin,\
				dailyrainin,\
				baromin,\
				weather,\
				clouds,\
				soiltempf,\
				soilmoisture,\
				leafwetness,\
				solarradiation,\
				UV,\
				visibility,\
				indoortempf,\
				indoorhumidity)
			number_of_rows = dbCursor.execute(sql)
			db.commit()
			# clean up after ourselves
			db.close()
		except Exception, e:
			print("Mysql Exception:",str(e)) 

	# log something
	print(str(datetime.now()),"::winddir[",winddir,"]:windspeedmph[",windspeedmph,"]:windgustmph[",windgustmph,"]:windgustdir[",windgustdir,"]:windspdmph_avg2m[",windspdmph_avg2m,"]:winddir_avg2m[",winddir_avg2m,"]:windgustmph_10m[",windgustmph_10m,"]:windgustdir_10m[",windgustdir_10m,"]:humidity[",humidity,"]:dewptf[",dewptf,"]:tempf[",tempf,"]:rainin[",rainin,"]:dailyrainin[",dailyrainin,"]:baromin[",baromin,"]:solarradiation[",solarradiation,"]:UV[",UV,"]:)")

        sys.stdout.flush()

	# wait on a bit
	time.sleep(readInterval)
