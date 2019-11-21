#!/usr/bin/python

import time
import RPi.GPIO as GPIO

class lock():
    def __init__(self):
        # config
        CHANNEL = 18
        FREQUENCY = 50
        self.TIME_SLEEP = 1

        # motor angles
        self.OPEN_LOCK = 0
        self.CLOSE_LOCK = 90

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(CHANNEL, GPIO.OUT)

        self.p = GPIO.PWM(CHANNEL, FREQUENCY)
        self.p.start(self.findValues(self.LOCK_ANGLE))
        time.sleep(TIME_SLEEP)

    # finds desired angle in degrees
    def findValues(self, angle):
        SLOPE = 8 / 180
        Y_INTERCEPT = 6.25
        
        return SLOPE * angle + Y_INTERCEPT

    def open_lock(self, open):
        try:
            if open:
                self.p.ChangeDutyCycle(self.findValues(self.OPEN_LOCK))
                time.sleep(self.TIME_SLEEP)
            else:
                self.p.ChangeDutyCycle(self.findValues(self.CLOSE_LOCK))
                time.sleep(self.TIME_SLEEP)
        except KeyboardInterrupt:
            self.p.ChangeDutyCycle(self.findValues(self.CLOSE_LOCK))
            time.sleep(self.TIME_SLEEP)
            pass