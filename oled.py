import ssd1306
from machine import Pin, I2C
i2c = I2C(-1, scl=Pin(12), sda=Pin(13))
oled_width = 128
oled_height = 32
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)


def show_loading(x, y, w, h, c):
    # w-width, h-height, c-color
    oled.fill_rect(x, y, w, h, c)
    oled.show()



# import machine
# from ssd1306_setup import WIDTH, HEIGHT, setup
# from writer import Writer
#
# # Font
# import freesans_cyr
#
# def test(text,use_spi=False):
#     ssd = setup(use_spi)  # Create a display instance
#     rhs = WIDTH -1
#     ssd.line(rhs - 20, 0, rhs, 20, 1)
#     square_side = 10
#     ssd.fill_rect(rhs - square_side, 0, square_side, square_side, 1)
#
#     wri = Writer(ssd, freesans_cyr)
#     Writer.set_textpos(ssd, 0, 0)  # verbose = False to suppress console output
#     wri.printstring(text)
#     # wri.printstring('12 Aug 2018\n')
#     # wri.printstring('10.30am')
#     ssd.show()
