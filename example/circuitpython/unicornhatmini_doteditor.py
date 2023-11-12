# Based on:
#   https://github.com/pimoroni/unicornhatmini-python/blob/master/library/unicornhatmini/__init__.py

import time
from digitalio import DigitalInOut, Direction, Pull
from unicornhatmini import UnicornHATMini, BUTTON_A, BUTTON_B, BUTTON_X, BUTTON_Y
import os
import time
import wifi
import socketpool
from adafruit_httpserver.server import HTTPServer
from adafruit_httpserver.request import HTTPRequest
from adafruit_httpserver.response import HTTPResponse
from adafruit_httpserver.methods import HTTPMethod
from adafruit_httpserver.mime_type import MIMEType

print("Connecting to WiFi")
wifi.radio.connect(os.getenv('CIRCUITPY_WIFI_SSID'), os.getenv('CIRCUITPY_WIFI_PASSWORD'))

print("Connected.")
pool = socketpool.SocketPool(wifi.radio)

server = HTTPServer(pool)

def webpage():
    return """<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<title>Dot Editor for Scroll pHAT HD and Pico W</title>
<script>
function toggle_pixel(e) {
    let x = e.cellIndex;
    let y = e.parentElement.rowIndex;
    var b, color;
    if (e.style.backgroundColor == '') {
        color = 'blue';
        b = 50;
    } else {
        color = '';
        b = 0;
    }
    fetch(`/led/${x}/${y}/${b}`)
        .then(function(r){ return r.text(); })
        .then(function(t){ e.style.backgroundColor = color; });
}
function scrollPhatTable() {
    var canvas = document.getElementById("canvas");
    let y = 7;
    let x = 17;
    for (var i = 0; i < y; i++) {
        var row = canvas.insertRow(-1);
        for (var j = 0; j < x; j++) {
            var cell = row.insertCell(-1);
            cell.onclick = function() { toggle_pixel(this); };
        }
    }
}
window.onload = function() { scrollPhatTable(); }
</script>
<style>
table {
  border-collapse: collapse;
  margin-bottom: 16px;
}
td {
  border: 1px solid gray;
  width: 32px;
  height: 32px;
  cursor: pointer;
}
</style>
</head>
<body>
<table id="canvas"></table>
<p>GET /led/[x(0-16)]/[y(0-6)]/[brightness(0-255)]</p>
</body>
</html>
"""

@server.route("/")
def base(request: HTTPRequest):
    with HTTPResponse(request, content_type=MIMEType.TYPE_HTML) as response:
        response.send(f"{webpage()}")

@server.route("/led/<px>/<py>/<c>")
def led(request: HTTPRequest, px: int, py: int, c: int):
    x = int(px)
    y = int(py)
    b = int(c)
    if x < 0 or y < 0 or b < 0 or 16 < x or 6 < y or 255 < b:
        body = "any parameter out of range"
    else:
        unicornhatmini.set_pixel(x, y, b, b, b)
        unicornhatmini.show()
        body = "%s(%s, %s)" % (b, x, y)
    with HTTPResponse(request, content_type=MIMEType.TYPE_HTML) as response:
        response.send(body)

print("Starting server...")
try:
    server.start(str(wifi.radio.ipv4_address))
    print("Listening on http://%s:80" % wifi.radio.ipv4_address)
except OSError:
    time.sleep(5)
    print("Failed start server. Restarting...")
    microcontroller.reset()

unicornhatmini = UnicornHATMini()

unicornhatmini.clear()
unicornhatmini.show()

buttons = []
for b in [BUTTON_A, BUTTON_B, BUTTON_X, BUTTON_Y]:
    buttons.append(DigitalInOut(b))
    buttons[-1].switch_to_input(pull=Pull.UP)
    time.sleep(0.5)

while True:
    try:
        server.poll()
    except Exception as e:
        print(e)
        continue