#!/usr/bin/env python

# reads data from an adafruit DHT11 temp/humidity sensor
# labels follow those set out in the Wunderground PWS API: 
#	http://wiki.wunderground.com/index.php/PWS_-_Upload_Protocol
#
# SOURCES:
#       * https://github.com/ControlEverythingCommunity/MPL3115A2/blob/master/Python/MPL3115A2.py
#       * https://github.com/johnwargo/pi_weather_station_simple
#       * https://www.domoticz.com/forum/viewtopic.php?t=839
# RETURNS: two objects for humidity and temperature
# CREATED: 2017-07-18
# MODIFIED: see https://github.com/dirtchild/weatherPi

import Adafruit_DHT
from SensorData import SensorReading 

def getReading():
	# pin the dht is connected to
	gpio = 23
	sensor = Adafruit_DHT.DHT11	

	hum, tem = Adafruit_DHT.read_retry(sensor, gpio)
	#DEBUG
	print hum
	print tem
	dhtHum = SensorReading("dht11", "humidity", hum, "%")
	dhtTem = SensorReading("dht11", "tempf", tem, "f")
	return (dhtTem,dhtHum)
