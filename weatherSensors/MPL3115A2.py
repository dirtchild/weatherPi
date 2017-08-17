#!/usr/bin/env python

# reads data from an adafruit DHT11 temp/humidity sensor
# labels follow those set out in the Wunderground PWS API:
#	http://wiki.wunderground.com/index.php/PWS_-_Upload_Protocol
#
# SOURCES:
#       * http://www.circuitbasics.com/how-to-set-up-the-dht11-humidity-sensor-on-the-raspberry-pi/
#       * https://github.com/adafruit/Adafruit_Python_DHT/blob/master/examples/AdafruitDHT.py
#       * https://github.com/johnwargo/pi_weather_station_simple
#       * https://www.domoticz.com/forum/viewtopic.php?t=839
# RETURNS: two objects for humidity and temperature
# CREATED: 2017-07-18
# MODIFIED: see https://github.com/dirtchild/weatherPi

from SensorData import SensorReading
from convertors import *
import smbus
import time

def getReading():
	# Get I2C bus
	bus = smbus.SMBus(1)

	# MPL3115A2 address, 0x60(96)
	# Select control register, 0x26(38)
	#		0xB9(185)	Active mode, OSR = 128, Altimeter mode
	bus.write_byte_data(0x60, 0x26, 0xB9)
	# MPL3115A2 address, 0x60(96)
	# Select data configuration register, 0x13(19)
	#		0x07(07)	Data ready event enabled for altitude, pressure, temperature
	bus.write_byte_data(0x60, 0x13, 0x07)
	# MPL3115A2 address, 0x60(96)
	# Select control register, 0x26(38)
	#		0xB9(185)	Active mode, OSR = 128, Altimeter mode
	bus.write_byte_data(0x60, 0x26, 0xB9)

	time.sleep(1)

	# MPL3115A2 address, 0x60(96)
	# Read data back from 0x00(00), 6 bytes
	# status, tHeight MSB1, tHeight MSB, tHeight LSB, temp MSB, temp LSB
	data = bus.read_i2c_block_data(0x60, 0x00, 6)

	# Convert the data to 20-bits
	tHeight = ((data[1] * 65536) + (data[2] * 256) + (data[3] & 0xF0)) / 16
	temp = ((data[4] * 256) + (data[5] & 0xF0)) / 16
	thisAltitude = tHeight / 16.0
	cTemp = temp / 16.0
	fTemp = c_to_f(cTemp)

	# MPL3115A2 address, 0x60(96)
	# Select control register, 0x26(38)
	#		0x39(57)	Active mode, OSR = 128, Barometer mode
	bus.write_byte_data(0x60, 0x26, 0x39)

	time.sleep(1)

	# MPL3115A2 address, 0x60(96)
	# Read data back from 0x00(00), 4 bytes
	# status, pres MSB1, pres MSB, pres LSB
	data = bus.read_i2c_block_data(0x60, 0x00, 4)

	# Convert the data to 20-bits
	pres = ((data[1] * 65536) + (data[2] * 256) + (data[3] & 0xF0)) / 16
	thisPressure = (pres / 4.0) / 3000.0

	mplPres = SensorReading("MPL3115A2", "baromin", thisPressure, "hpa")
	mplTem = SensorReading("MPL3115A2", "tempf", fTemp, "f")
	mplAlt = SensorReading("MPL3115A2", "altitude", thisAltitude, "m")

	return (mplTem,mplPres,mplAlt)
