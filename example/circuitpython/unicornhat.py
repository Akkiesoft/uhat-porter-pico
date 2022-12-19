# 2022 Akkiesoft
# MIT
#
# ORIGINAL:
#   SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#   SPDX-License-Identifier: MIT

"""
CircuitPython Essentials NeoPixel example for uHAT Porter Pico
*Test for Pimoroni Unicorn HAT
"""
import time
from rainbowio import colorwheel
import neopixel

import uhat_porter_pico_type_s as board_bcm
#import uhat_porter_pico_type_p as board_bcm

pixel_pin = board_bcm.BCM18
num_pixels = 64
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.03, auto_write=False)

def color_chase(color, wait):
    for i in range(num_pixels):
        pixels[i] = color
        time.sleep(wait)
        pixels.show()
    time.sleep(0.5)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            pixels[i] = colorwheel(rc_index & 255)
        pixels.show()
        time.sleep(wait)


RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)

while True:
    pixels.fill(RED)
    pixels.show()
    # Increase or decrease to change the speed of the solid color change.
    time.sleep(1)
    pixels.fill(GREEN)
    pixels.show()
    time.sleep(1)
    pixels.fill(BLUE)
    pixels.show()
    time.sleep(1)

    color_chase(RED, 0.1)  # Increase the number to slow down the color chase
    color_chase(YELLOW, 0.1)
    color_chase(GREEN, 0.1)
    color_chase(CYAN, 0.1)
    color_chase(BLUE, 0.1)
    color_chase(PURPLE, 0.1)

    rainbow_cycle(0)  # Increase the number to slow down the rainbow