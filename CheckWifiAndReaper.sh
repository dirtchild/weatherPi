# created: 2018-08-14 dirtchild@github
# borrowed from: https://aruljohn.com/code/shell/wifi-reconnect.html

exportFile="/home/exports/weather_cache.influx"

DATE=`date '+%Y-%m-%d %H:%M:%S'`

# Ping to the router
ping -c5 10.0.0.254 > /dev/null

# If the return code from ping ($?) is not 0 (meaning there was an error)
if [ $? != 0 ]; then
    echo "[REAPER] $DATE wlan0 down, reconnecting"

    # Restart the wireless interface
    ifdown --force wlan0
    sleep 5
    ifup wlan0
else
    # we have wifi. see if there's anythign that needs xferring
    influx_inspect export -datadir /var/lib/influxdb/data -waldir /var/lib/influxdb/wal -out "$exportFile" -database weather_cache
    grep \, $exportFile | grep \= > $exportFile.trimmed

    # if we have anything
    if [ -s $exportFile.trimmed ]; then
	echo "[REAPER] $DATE WIFI up, data in DB, sending"
    	# send it to the remote if it's there
	if curl -i -XPOST "http://home:8086/write?db=home_environment" --data-binary @$exportFile.trimmed; then
		echo "[REAPER] $DATE data in DB, sent, clearing local DB"
    	 	# clear the DB
 		curl -i -XPOST "http://127.0.0.1:8086/write?db=weather_cache&q=DROP+MEASUREMENT+external"
	fi
    fi

fi
