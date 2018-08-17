# created: 2018-08-14 dirtchild@github
# borrowed from: https://aruljohn.com/code/shell/wifi-reconnect.html

exportFile="/home/exports/weather_cache.influx"

# Ping to the router
ping -c5 10.0.0.254 > /dev/null

# If the return code from ping ($?) is not 0 (meaning there was an error)
if [ $? != 0 ]; then
    # Restart the wireless interface
    ifdown --force wlan0
    sleep 5
    ifup wlan0
    echo "wlan0 reconnected at `date`"
else
    # we have wifi. see if there's anythign that needs xferring
    influx_inspect export -datadir /var/lib/influxdb/data -waldir /var/lib/influxdb/wal -out "$exportFile" -database weather_cache
    grep \, $exportFile | grep \= > $exportFile.trimmed

    # if we have anything
    if [ -s $exportFile.trimmed ]; then
    	# clear the DB
 	curl -i -XPOST "http://127.0.0.1:8086/write?db=weather_cache&q=DROP+MEASUREMENT+external"

    	# send it to the remote
	curl -i -XPOST "http://127.0.0.1:8086/write?db=weather_cache" --data-binary @$exportFile.trimmed
    fi

fi
