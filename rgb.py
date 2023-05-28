#!/usr/bin/python
import socket
import os
import re
import time
from rpi_ws281x import Adafruit_NeoPixel, Color


# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms / 1000.0)


if __name__ == "__main__":
    TOTAL_LED_COUNT = 24
    R = 0
    G = 0
    B = 0

    strip = Adafruit_NeoPixel(TOTAL_LED_COUNT, 18, 800000, 5, False, 255)
    strip.begin()
    colorWipe(strip, Color(0, 0, 0))

    # Set the path for the Unix socket
    socket_path = '/var/www/vhosts/rgb.local/rgb_socket'

    # remove the socket file if it already exists
    try:
        os.unlink(socket_path)
    except OSError:
        if os.path.exists(socket_path):
            raise

    server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    server.bind(socket_path)
    server.listen(1)
    os.chown(socket_path, 33, 33)
    connection, client_address = server.accept()

    try:
        while True:
            data = connection.recv(1024)
            if not data:
                # connection lost, reestablish connection
                connection, client_address = server.accept()
                continue
            rgb = data.decode()
            if re.match("^[0-9A-Fa-f]{6}$", rgb):
                colorWipe(strip, Color(
                    int(rgb[0:2], 16),
                    int(rgb[2:4], 16),
                    int(rgb[4:6], 16)),
                    10
                )
    finally:
        colorWipe(strip, Color(0, 0, 0), 10)
        connection.close()
        os.unlink(socket_path)
