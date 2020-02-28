import mfrc522
from oled import oled, show_loading
# from oled import test



# def post_api(tag, url):
#     data = {'body':{'tag':'%s'}} % tag
#     headers = {'Content-Type': 'application/json'}
#
#     r = urequests.post(url, data=data, headers=headers)
#     print(r.json())


def read(url=None):
    import urequests
    # import ur as urequests

    rdr = mfrc522.MFRC522(14, 13, 12, 2, 15)

    try:
        while True:

            (stat, tag_type) = rdr.request(rdr.REQALL)

            oled.fill(0)
            oled.show()
            show_loading(56, 8, 16, 16, 1)

            print(tag_type)

            if stat == rdr.OK:
                show_loading(56, 8, 16, 16, 0)

                (stat, raw_uid) = rdr.anticoll()

                if stat == rdr.OK:
                    for i in range(1, 129, 15):
                        show_loading(i, 28, 16, 5, 1)
                    tag_id = "0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3])
                    oled.fill(0)
                    oled.text('New card', 0, 0)
                    oled.text('uid: '+ tag_id, 0, 10)
                    oled.show()

                    data = '{"body":{"tag":"%s", "student":"", "scanned":null}}' % str(tag_id)
                    headers = {'Content-Type': 'application/json'}
                    # try:
                    if url != None:
                        r = urequests.post(url, data=data, headers=headers)
                        # r = urequests.get(url)
                        oled.fill(0)
                        oled.text(str(r.json()), 0, 10)
                        oled.show()
                        # test(str(r.json()))3
                        print(r.json())
                    else:
                        continue
                    # except:
                    #     oled.fill(0)
                    #     oled.text('Error. Retry', 0, 10)
                    #     oled.show()
                    #     print('error post api')
                else:
                    oled.text('Error. Retry', 0, 10)
                    oled.show()
                    print('error')


    except KeyboardInterrupt:
        print('Bye')

