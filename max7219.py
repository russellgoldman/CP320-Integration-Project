import RPi.GPIO as GPIO
from time import sleep, strftime
from datetime import datetime

from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.led_matrix.luma.led_matrix.device import max7219
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, LCD_FONT

class display():
    def __init__(self):
        # serial
        SERIAL_PORT = 0
        SERIAL_DEVICE = 0

        # device
        DEVICE_WIDTH = 32
        DEVICE_HEIGHT = 8
        DEVICE_BLOCK_ORIENTATION = -90
        DEVICE_CONTRAST = 5

        # virtual
        VIRTUAL_WIDTH = 32
        VIRTUAL_HEIGHT = 16

        self.serial = spi(port=SERIAL_PORT, device=SERIAL_DEVICE, gpio=noop())
        self.device = max7219(self.serial, width=DEVICE_WIDTH, height=DEVICE_HEIGHT, block_orientation=DEVICE_BLOCK_ORIENTATION)
        self.device.contrast(DEVICE_CONTRAST)
        self.virtual = viewport(self.device, width=VIRTUAL_WIDTH, height=VIRTUAL_HEIGHT)
    
    def runMAX7219(self, code, mode):
        try:
            # draw config
            DRAW_START = 0
            DRAW_END = 1
            FILL = "WHITE"

            # draw text
            CONFIRM = "O"
            REJECT = "X"
            TOO_FAR = "^"

            while True:
                with canvas(self.virtual) as draw:
                    if mode == "confirm":
                        text(draw, (DRAW_START, DRAW_END), CONFIRM, fill=FILL, font=proportional(CP437_FONT))
                    elif mode == "reject":
                        text(draw, (DRAW_START, DRAW_END), REJECT, fill=FILL, font=proportional(CP437_FONT))
                    elif mode == "too_far":
                        text(draw, (DRAW_START, DRAW_END), TOO_FAR, fill=FILL, font=proportional(CP437_FONT))

        except KeyboardInterrupt:
            GPIO.cleanup()