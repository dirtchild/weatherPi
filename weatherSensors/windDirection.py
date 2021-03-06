#!/usr/bin/env python

# reads data from wind direction thingy (see README)
# labels follow those set out in the Wunderground PWS API:
#	http://wiki.wunderground.com/index.php/PWS_-_Upload_Protocol
#
# SOURCES:
# RETURNS: two objects for humidity and temperature
# CREATED: 2017-08-02
# ORIGINAL SOURCE: https://github.com/dirtchild/weatherPi [please do not remove this line]
# MODIFIED: see https://github.com/dirtchild/weatherPi

from SensorData import SensorReading
import time
import Adafruit_ADS1x15
import convertors
import windDirection
import sys
sys.path.append("../")
from config import *

def getReading():
	# Choose a gain of 1 for reading voltages from 0 to 4.09V.
	# Or pick a different gain to change the range of voltages that are read:
	#  - 2/3 = +/-6.144V
	#  -   1 = +/-4.096V
	#  -   2 = +/-2.048V
	#  -   4 = +/-1.024V
	#  -   8 = +/-0.512V
	#  -  16 = +/-0.256V
	# See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.
	GAIN = 16

	# the channel on the ADC to use
	CHANNEL = 0

	# Create an ADS1115 ADC (16-bit) instance and do stuff with it
	adc = Adafruit_ADS1x15.ADS1115()
	adc.start_adc(CHANNEL, gain=GAIN)
	start = time.time()
	value = 0
	totalVoltage = 0
	cnt = 0
	#DEBUG
	#print("[PRE]adc.get_last_result()[",adc.get_last_result(),"]")
	while (time.time() - start) <= 5.0:
		# will sometimes give negative results
		thisRead = -1
		while thisRead < 1:
		    thisRead = adc.get_last_result()
		#DEBUG: finding they are about a decimal place out
		#DEBUG: hacky
		#DEBUG
		#print(cnt,": thisRead[",thisRead,"]")
		totalVoltage += thisRead / 10 #DEBUG: /10 to get it into a measurable range. this is bad and wrong
		cnt += 1
		time.sleep(0.5)
	#DEBUG
	#print("[POST]adc.get_last_result()[",adc.get_last_result(),"]")
	# Stop continuous conversion.  After this point you can't get data from get_last_result!
	adc.stop_adc()
	avgVoltage = totalVoltage / cnt

	#DEBUG
	#print("avgVoltage[",avgVoltage,"] = totalVoltage[",totalVoltage,"] / cnt[",cnt,"] (G:[",GAIN,"] C:[",CHANNEL,"])")

	return(SensorReading("winddir", "winddir", convertors.voltToDeg(avgVoltage,WIND_READ_VOLT,WIND_DIR_MOUNT_ADJ), "degree angle"))

# for testing
def main():
    print(windDirection.getReading())
if __name__ == "__main__": main()
