# import network
# wifi = network.WLAN(network.STA_IF)
# wifi.active(True)
# wifi.connect('Senkiv', 'senkiv0502036356')
# wifi.isconnected()

#
# url = 'https://4b0e4dbd.ngrok.io/api/scan/'

def connect():
    import network

    ssid = "Senkiv"
    password = "senkiv0502036356"

    # ssid = "XPERIA XZ1"
    # password = "12345678"

    station = network.WLAN(network.STA_IF)

    if station.isconnected() == True:
        print("Already connected")
        return

    station.active(True)
    station.connect(ssid, password)

    while station.isconnected() == False:
        pass

    print("Connection successful")
    print(station.ifconfig())


