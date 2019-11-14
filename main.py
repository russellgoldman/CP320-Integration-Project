import time
import RPi.GPIO as GPIO
from keypad import keypad
from max7219 import display
from infared_sensor import sensor
from servo_motor import lock
 
GPIO.setwarnings(False)
 
if __name__ == '__main__':
    # Initialize
    kp = keypad()
    s = sensor()
    l = lock()
    d = display()
 
    # check if the infared sensor detects someone
    ok = False
    ok = s.check_reading()

    ###### 4 Digit wait ######
    seq = []
    for i in range(4):
        digit = None
        while digit == None:
            digit = kp.getKey()
        seq.append(digit)
        print(digit)
        time.sleep(0.4)
 
    # Check digit code
    print(seq)

    if not ok:
        d.runMAX7219(seq, "too_far")
    elif seq == [1, 2, 3, '#']:
        print("Code accepted")
        d.runMAX7219(seq, "confirm")
        s.open_lock(True)
    else:
        d.runMAX7219(seq, "reject")