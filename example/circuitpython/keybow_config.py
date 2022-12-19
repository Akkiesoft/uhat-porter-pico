from adafruit_hid.keycode import Keycode

# 0 = Keybow, 1 = Keybow mini.
keybow_type = 1

if keybow_type:
  colors = [
      (255,   0,   0),
      (  0, 255,   0),
      (  0,   0, 255),
  ]
  keycodes = [
      [Keycode.A],
      [Keycode.B],
      [Keycode.C],
  ]
else:
  colors = [
      (255,   0,   0),
      (  0, 255,   0),
      (  0,   0, 255),
      (255,   0,   0),
      (  0, 255,   0),
      (  0,   0, 255),
      (255,   0,   0),
      (  0, 255,   0),
      (  0,   0, 255),
      (255,   0,   0),
      (  0, 255,   0),
      (  0,   0, 255),
  ]
  keycodes = [
      [Keycode.A],
      [Keycode.B],
      [Keycode.C],
      [Keycode.D],
      [Keycode.E],
      [Keycode.F],
      [Keycode.G],
      [Keycode.H],
      [Keycode.I],
      [Keycode.J],
      [Keycode.K],
      [Keycode.L],
  ]