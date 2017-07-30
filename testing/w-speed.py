#!/usr/bin/python3

# from: https://raw.githubusercontent.com/hamishcunningham/pi-tronics/master/environment/rain.py
# hacked 2017-07-29 docil@github


import RPi.GPIO as GPIO
import time

# which GPIO pin the gauge is connected to
PIN = 13
# file to log rainfall data in
LOGFILE = "./logs/w-speed.csv"

GPIO.setmode(GPIO.BCM)  
GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# keep track of how many ticks on the sensor
wspeed = 0

# in MPH as per http://mile-end.co.uk/blog/?p=86
perTick= 1.492

# the call back function for each bucket tip
def cb(channel):
	global wspeed
        wspeed = wspeed+perTick
	
# register the call back for pin interrupts
GPIO.add_event_detect(PIN, GPIO.FALLING, callback=cb, bouncetime=300)

# open the log file
file = open(LOGFILE, "a")

# display and log results
while True:
	line = "%s, %.2fMph" % (time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime()), wspeed)
	print(line)
	file.write(line + "\n")
	file.flush()
	wspeed = 0
	time.sleep(5)

# close the log file and exit nicely
file.close()
GPIO.cleanup()
