import RPi.GPIO as GPIO
from time import sleep, strftime
from datetime import datetime

from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.led_matrix.device import max7219
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, LCD_FONT

serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, width=32, height=8, block_orientation=-90)
device.contrast(5)
virtual = viewport(device, width=32, height=16)
show_message(device, 'Raspberry Pi MAX7219', fill="white", font=proportional(LCD_FONT), scroll_delay=0.08)

def runMAX7219(code, mode):
    try:
        print("Code: %s" % code)
        while True:
            with canvas(virtual) as draw:
                if mode == "confirm":
                    text(draw, (0, 1), "X", fill="white", font=proportional(CP437_FONT))
                elif mode == "reject":
                    text(draw, (0, 1), "O", fill="white", font=proportional(CP437_FONT))
                elif mode == "too_far":
                    text(draw, (0, 1), "^", fill="white", font=proportional(CP437_FONT))

    except KeyboardInterrupt:
        GPIO.cleanup()