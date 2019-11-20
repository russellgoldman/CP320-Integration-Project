#!/usr/bin/python

import time
import RPi.GPIO as GPIO

class lock():
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(18, GPIO.OUT)

        self.p = GPIO.PWM(18, 50)  # channel=18 frequency=60Hz
        self.p.start(self.findValues(0))
        time.sleep(1)

    def findValues(self, angle):
        # finds desired angle in degrees
        return 8/180 * angle + 6.25

    def open_lock(self, open):
        try:
            if open:
                self.p.ChangeDutyCycle(self.findValues(90))  # 90 degrees
                time.sleep(1)
            else:
                self.p.ChangeDutyCycle(self.findValues(0))
                time.sleep(1)
        except KeyboardInterrupt:
            self.p.ChangeDutyCycle(self.findValues(0))
            time.sleep(1)
            pass