# for Pimoroni 0.96" SPI Colour LCD (160x80) Breakout
#   https://shop.pimoroni.com/products/0-96-spi-colour-lcd-160x80-breakout

import uhat_porter_pico_type_p3 as board_bcm
from busio import SPI
import displayio
from adafruit_display_shapes.rect import Rect
from adafruit_st7735r import ST7735R

displayio.release_displays()
spi = SPI(clock=board_bcm.BCM11, MOSI=board_bcm.BCM10)
display_bus = displayio.FourWire(
    spi, command=board_bcm.BCM9, chip_select=board_bcm.BCM7, baudrate=62400000
)
display = ST7735R(
    display_bus, width=160, height=80, colstart=26, rowstart=1, rotation=270, invert=True
)
splash = displayio.Group()
display.show(splash)

splash.append(Rect(  0,   0, 160,  80, fill=0x00aa8d))
splash.append(Rect(  0,   0,   1,   1, fill=0x000000))
splash.append(Rect(  0,  79,   1,   1, fill=0x000000))
splash.append(Rect(159,   0,   1,   1, fill=0x000000))
splash.append(Rect(159,  79,   1,   1, fill=0x000000))

while True:
    pass