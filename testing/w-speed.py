#!/usr/bin/python3

# from: https://raw.githubusercontent.com/hamishcunningham/pi-tronics/master/environment/rain.py
# hacked 2017-07-29 docil@github


import RPi.GPIO as GPIO
import time

# which GPIO pin the gauge is connected to
PIN = 13
# file to log rainfall data in
LOGFILE = "wsp-log.csv"

GPIO.setmode(GPIO.BCM)  
GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# variable to keep track of how much rain
wspeed = 0

# the call back function for each bucket tip
def cb(channel):
	global wspeed
	
# register the call back for pin interrupts
GPIO.add_event_detect(PIN, GPIO.FALLING, callback=cb, bouncetime=300)

# open the log file
file = open(LOGFILE, "a")

# display and log results
while True:
	line = "%i, %f" % (time.time(), wspeed)
	print(line)
	file.write(line + "\n")
	file.flush()
	wspeed = 0
	time.sleep(5)

# close the log file and exit nicely
file.close()
GPIO.cleanup()
