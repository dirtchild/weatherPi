#!/usr/bin/env python

# reads data from an adafruit DHT11 temp/humidity sensor
# SOURCES:
#       * https://github.com/ControlEverythingCommunity/MPL3115A2/blob/master/Python/MPL3115A2.py
#       * https://github.com/johnwargo/pi_weather_station_simple
#       * https://www.domoticz.com/forum/viewtopic.php?t=839
# RETURNS: two objects for humidity and temperature
# CREATED: 2017-07-18
# MODIFIED: see https://github.com/dirtchild/weatherPi

import Adafruit_DHT
import SensorData.SensorReading

def getDHT11():
	# pin the dht is connected to
	gpio = 23

	hum, tem = Adafruit_DHT.read_retry(11, self.gpio)
	dhtHum = SensorReading("dht11", "humidity", hum, "%")
	dhtTem = SensorReading("dht11", "temperature", tem, "f")
	return (dhtTem,dhtHum)
