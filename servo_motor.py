import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

def findValues(angle):
# finds desired angle in degrees
    return 8/180 * angle + 6.25

p = GPIO.PWM(12, 50)  # channel=12 frequency=60Hz
p.start(6)
time.sleep(1)

def open_lock(open):
    try:
        if open:
            p.ChangeDutyCycle(findValues(90))  # 90 degrees
            time.sleep(1)
        else:
            p.ChangeDutyCycle(findValues(0))
    except KeyboardInterrupt:
        p.ChangeDutyCycle(findValues(0))
        pass

    p.stop()
    GPIO.cleanup()