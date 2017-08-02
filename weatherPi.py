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

########################################################################
# imports
from MODULES import weatherSensors, utilities
import time

########################################################################
# config
# in seconds
readInterval = 60

########################################################################
# MAIN

# fire off our time-dependent sensors (wind speed, rainfall etc)

# loop forever. could have used threads, too big of a hammer for the job
while True:
	# read in all of our sensors for the general checks

	# do something extra every N seconds - gusts, rain??? is this needed
	time.sleep(readInterval)