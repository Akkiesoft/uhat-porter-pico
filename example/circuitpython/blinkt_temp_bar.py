# RP2040 Temperature bar for Pimoroni BLINKT!
# 2023 Akkiesoft
# MIT
import uhat_porter_pico_type_p3 as board_bcm

import adafruit_dotstar as dotstar
import time
import microcontroller

min_temp = 20
max_temp = 38
temp_range = max_temp - min_temp
dot_count = 7
brightness = 48

dots = dotstar.DotStar(board_bcm.BCM24, board_bcm.BCM23, 30, brightness=0.1)

while True:
    temp = microcontroller.cpu.temperature
    mapped_temp = (((temp - min_temp) * dot_count) / temp_range)
    decimals = int((mapped_temp - int(mapped_temp)) * 100)
    mapped_decimals = int(decimals * brightness / 99)

    for i in range(0, 8):
        if i <= mapped_temp:
            dots[i] = (brightness, brightness, brightness)
        elif i <= mapped_temp + 1:
            dots[i] = (mapped_decimals, mapped_decimals, mapped_decimals)
        else:
            dots[i] = (0, 0, 0)
    time.sleep(0.1)