url = 'https://d3d9d888.ngrok.io/api/scan/'
# import urequests
# data = '{"body":{"tag":"mitka", "student":"", "scanned":null}}'
# headers = {'Content-Type': 'application/json'}
# r = urequests.post(url, data=data, headers=headers)


def connect(ssid="Senkiv", password="senkiv0502036356"):
    import network

    # ssid = "Senkiv"
    # password = "senkiv0502036356"

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
    print('network config: ',station.ifconfig())


def disconnect():
    import network

    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(False)
    ap_if = network.WLAN(network.AP_IF)
    ap_if.active(False)

    print("Disconnection successful")
    print('network sta config: ', sta_if.ifconfig())
    print('network ap config: ', ap_if.ifconfig())
