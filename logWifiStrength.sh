#! /bin/bash

( echo -n `date +"[%Y-%m-%d %H:%M:%S]"`;/sbin/iwconfig wlan0 | grep Link ) >> /var/log/wifi-quality.log



