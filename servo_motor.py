#!/usr/bin/python

import time
import RPi.GPIO as GPIO

class lock():
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(18, GPIO.OUT)

        self.p = GPIO.PWM(18, 50)  # channel=18 frequency=60Hz
        self.p.start(6)
        time.sleep(1)

    def findValues(angle):
    # finds desired angle in degrees
        return 8/180 * angle + 6.25

    def open_lock(self, open):
        try:
            if open:
                self.p.ChangeDutyCycle(findValues(90))  # 90 degrees
                time.sleep(1)
            else:
                self.p.ChangeDutyCycle(findValues(0))
        except KeyboardInterrupt:
            self.p.ChangeDutyCycle(findValues(0))
            pass

        self.p.stop()
        GPIO.cleanup()