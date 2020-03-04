def read(url):
    import mfrc522
    from oled import oled, show_loading
    import urequests

    # Init rfid reader
    rdr = mfrc522.MFRC522(14, 13, 12, 2, 15)

    try:
        while True:
            # Check antenna
            (stat, tag_type) = rdr.request(rdr.REQALL)

            # Show animation on esp display
            oled.fill(0)
            oled.show()
            show_loading(56, 8, 16, 16, 1)

            print(tag_type)

            if stat == rdr.OK:
                show_loading(56, 8, 16, 16, 0)

                # Get data about tag
                (stat, raw_uid) = rdr.anticoll()

                if stat == rdr.OK:
                    # get tag id
                    tag_id = "0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3])
                    oled.fill(0)
                    oled.text('IDENTIFICATION', 0, 10)
                    oled.text('...', 0, 20)
                    oled.show()

                    data = '{"body":{"tag":"%s", "student":"", "scanned":null}}' % str(tag_id)
                    headers = {'Content-Type': 'application/json'}
                    try:
                        # Share tag id to api
                        r = urequests.post(url, data=data, headers=headers)
                        oled.fill(0)
                        oled.text(str(r.json()).upper(), 0, 10)
                        oled.show()
                        print(r.json())
                    except:
                        oled.fill(0)
                        oled.text('ERROR. RETRY', 0, 10)
                        oled.show()
                        print('error post api')
                else:
                    oled.text('ERROR. RETRY', 0, 10)
                    oled.show()
                    print('error')

    except KeyboardInterrupt:
        print('Bye')
