import esp
import network
import os
import webrepl

# TODO: put these in a secrets file
WLAN_SSID = os.getenv("WLAN_SSID")
WLAN_PASS = os.getenv("WLAN_PASS")


def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(WLAN_SSID, WLAN_PASS)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())


esp.osdebug(None)

do_connect()
webrepl.start()
