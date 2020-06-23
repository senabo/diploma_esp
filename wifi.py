def connect(ssid="ssid", password="pass"):
    import network

    station = network.WLAN(network.STA_IF)

    if station.isconnected() == True:
        print("Already connected")
        return

    station.active(True)
    station.connect(ssid, password)

    while station.isconnected() == False:
        pass

    print("Connection successful")
    print('network config: ', station.ifconfig())


def disconnect():
    import network

    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(False)
    ap_if = network.WLAN(network.AP_IF)
    ap_if.active(False)

    print("Disconnection successful")
    print('network sta config: ', sta_if.ifconfig())
    print('network ap config: ', ap_if.ifconfig())
