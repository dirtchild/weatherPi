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
from weatherSensors import eventSensor as eventSensor
import MySQLdb as my
import time
import urllib2

# fire off our time-dependent sensors (wind speed, rainfall etc)
wSpeed = eventSensor(W_SPD_GPIO, W_SPD_CALIBRATION, "wind speed events", "w_spd", "MPH", W_SPD_EVENTS_PERIOD)
rain = eventSensor(RAIN_GPIO, RAIN_CALIBRATION, "rain events", "rain", "mm", RAIN_EVENTS_PERIOD)

# DB connection
db = my.connect(host=db_host,user=db_user,passwd=db_pwd,db=db_db)
dbCursor = db.cursor()

# URL prep stuff for wunderground upload
# DEBUG

# loop forever.
while True:
	# read in all of our single check sensors for thsi run
	dhtTem,dhtHum = weatherSensors.DHT11.getReading()
	mplTem,mplPres,mplAlt = weatherSensors.MPL3115A2.getReading()
	uv = weatherSensors.uv.getReading()
	windDir = weatherSensors.windDirection.getReading()
	windSpeedNow = wSpeed.getLast()
	windSpdMph_avg2m = wSpeed.getPeriodAverage("windSpdMph_avg2m",120)
	rainIn = rain.getPeriodTotal("rainIn", 3600)
	dailyRainIn = mmToInches(rain.getPeriodTotal("dailyRainIn", 86400))

	# setup our reading variables to make things better for human brains
	# and to amke the rest of this easier
	winddir = windDir.value
	windspeedmph = windSpeedNow.value
	windgustmph = "Null"
	windgustdir = "Null"
	windspdmph_avg2m = windSpdMph_avg2m.value
	winddir_avg2m = "Null"
	windgustmph_10m = "Null"
	windgustdir_10m = "Null"
	humidity = dhtHum.value
	dewptf = dewpointF(tempF.value, dhtHum.value)
	tempf = (mplTem.value + dhtTem.value) / 2
	rainin = mmToInches(rainIn.value)
	dailyrainin = mmToInches(dailyRainIn.value)
	baromin = mplPres.value
	weather = "Null"
	clouds = "Null"
	soiltempf = "Null"
	soilmoisture = "Null"
	leafwetness = "Null"
	solarradiation = "Null"
	UV = uv.value
	visibility = "Null"
	indoortempf = "Null"
	indoorhumidity = "Null"

	# do the work
	if WEATHER_UPLOAD == True:
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
		except:
			print("Exception:", sys.exc_info()[0], SLASH_N)

		# write to our database
		sql = "insert into %s VALUES(Null, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d)" % \
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
		number_of_rows = cursor.execute(sql)
		db.commit()

	# log something
	print(str(datetime.now()),"::winddir[",winddir,"]:windspeedmph[",windspeedmph,"]:windgustmph[",windgustmph,"]:windgustdir[",windgustdir,"]:windspdmph_avg2m[",windspdmph_avg2m,"]\
		:winddir_avg2m[",winddir_avg2m,"]:windgustmph_10m[",windgustmph_10m,"]:windgustdir_10m[",windgustdir_10m,"]:humidity[",humidity,"]:dewptf[",dewptf,"]\
		:tempf[",tempf,"]:rainin[",rainin,"]:dailyrainin[",dailyrainin,"]:baromin[",baromin,"]:solarradiation[",solarradiation,"]:UV[",UV,"]:)")


	# wait on a bit
	time.sleep(readInterval)

# clean up after ourselves
db.close()
