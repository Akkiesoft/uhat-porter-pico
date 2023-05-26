# Test for Pimoroni BLINKT!
# 2022 Akkiesoft
# MIT

# type_s or type_p3 are recommend.
# type_p is slow to show.
#import uhat_porter_pico_type_s as board_bcm
import uhat_porter_pico_type_p3 as board_bcm

import adafruit_dotstar as dotstar
import time
import random

dots = dotstar.DotStar(board_bcm.BCM24, board_bcm.BCM23, 30, brightness=0.01)

while True:
  for i in range(0,8):
    r = random.randrange(255)
    g = random.randrange(255)
    b = random.randrange(255)
    dots[i] = (r, g, b)
    dots.show()
  time.sleep(0.1)