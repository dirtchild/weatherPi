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
import MySQLdb as my

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
	rainIn = mmToInches(rain.getPeriodTotal("rainIn", 3600))
	dailyRainIn = mmToInches(rain.getPeriodTotal("dailyRainIn", 86400))

	# calculate a few thigns
	tempF = (mplTem + dhtTem) / 2
	dpF = dewpointF(tempF, dhtHum)

	# setup our reading variables to make things better for human brains
	winddir = 
	windspeedmph =
	windgustmph = "Null"
	windgustdir = "Null"
	windspdmph_avg2m = 
	winddir_avg2m = "Null"
	windgustmph_10m = "Null"
	windgustdir_10m = "Null"
	humidity =
	dewptf = 
	tempf =
	rainin =
	dailyrainin =
	baromin =
	weather = "Null"
	clouds = "Null"
	soiltempf = "Null"
	soilmoisture = "Null"
	leafwetness = "Null"
	solarradiation = "Null"
	UV = 
	visibility = "Null"
	indoortempf = "Null"
	indoorhumidity = "Null"
	
	# do the work
	if WEATHER_UPLOAD == True:
		# write to wunderground
		#DEBUG
		print "[DEBUG]	writing stuff to online stuff"
		
		# write to our database
		sql = "insert into %s VALUES(Null, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d, %d)" % \
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
	
	# log something?
	print "[DEBUG] log to logFile"
	
	# wait on a bit
	time.sleep(readInterval)

# clean up after ourselves
db.close()

