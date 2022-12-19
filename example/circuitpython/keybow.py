# Pimoroni Keybow sample for uHAT Poter Pico
# 2022 Akkiesoft
# MIT

import uhat_porter_pico_type_s as board_bcm
#import uhat_porter_pico_type_p as board_bcm
import digitalio
from time import sleep
import adafruit_dotstar as dotstar
import usb_hid
from adafruit_hid.keyboard import Keyboard

from keybow_config import keybow_type, colors, keycodes

def led_position(p):
    if keybow_type:
        return 2 - p
    else:
        # i = 左からn個目-1
        i = p % 3
        # 横側のベースの数(i * 4) + 縦方向の数(下から1段〜4段)
        return i * 4 + (4 - int((p + 3 - i) / 3))

dots = dotstar.DotStar(board_bcm.BCM11, board_bcm.BCM10, 30, brightness=0.5)

keyboard=Keyboard(usb_hid.devices)
if keybow_type:
    buttons = [
        digitalio.DigitalInOut(board_bcm.BCM17),
        digitalio.DigitalInOut(board_bcm.BCM22),
        digitalio.DigitalInOut(board_bcm.BCM6)
    ]
else:
    buttons = [
        digitalio.DigitalInOut(board_bcm.BCM17),
        digitalio.DigitalInOut(board_bcm.BCM27),
        digitalio.DigitalInOut(board_bcm.BCM23),
        digitalio.DigitalInOut(board_bcm.BCM22),
        digitalio.DigitalInOut(board_bcm.BCM24),
        digitalio.DigitalInOut(board_bcm.BCM5),
        digitalio.DigitalInOut(board_bcm.BCM6),
        digitalio.DigitalInOut(board_bcm.BCM12),
        digitalio.DigitalInOut(board_bcm.BCM13),
        digitalio.DigitalInOut(board_bcm.BCM20),
        digitalio.DigitalInOut(board_bcm.BCM16),
        digitalio.DigitalInOut(board_bcm.BCM26),
    ]
for b in buttons:
    b.switch_to_input(pull=digitalio.Pull.UP)

a = len(buttons) - 1
sw = [0] * len(buttons)

while True:
    for i,b in enumerate(buttons):
        if not b.value:
            if not sw[i]:
                try:
                    dots[led_position(i)] = colors[i]
                    for k in keycodes[i]:
                        keyboard.press(k)
                        sleep(0.05)
                    sw[i] = 1
                except:
                    pass
        else:
            if sw[i]:
                keyboard.release_all()
                dots[led_position(i)] = (0, 0, 0)
                sw[i] = 0
    sleep(0.02)