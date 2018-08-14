# created: 2018-08-14 dirtchild@github
# borrowed from: https://aruljohn.com/code/shell/wifi-reconnect.html

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
    #QUERY THE LOCAL CACHE DB
    #SEND ANYTHING TO REMOTE
fi
