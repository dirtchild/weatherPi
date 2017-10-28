#! /bin/bash

( echo -n `date +"[%Y-%m-%d %H:%M:%S]"`;iwconfig wlan0 | grep Link ) >> /var/log/wifi-quality.log


