import ssd1306
from machine import Pin, I2C

# Setting pins on esp
i2c = I2C(-1, scl=Pin(5), sda=Pin(4))
oled_width = 128
oled_height = 32

#Initialization esp oled display
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)


def show_loading(x, y, w, h, c):
    # w-width, h-height, c-color
    oled.fill_rect(x, y, w, h, c)
    oled.show()
