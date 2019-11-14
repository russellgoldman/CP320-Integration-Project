import time
import RPi.GPIO as GPIO
from keypad import keypad
from max7219 import runMAX7219
from infared_sensor import check_reading
 
GPIO.setwarnings(False)
 
if __name__ == '__main__':
    # Initialize
    kp = keypad()
 
    # check if the infared sensor detects someone
    ok = False
    ok = check_reading()

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
        runMAX7219(seq, "too_far")
    elif seq == [1, 2, 3, '#']:
        print("Code accepted")
        runMAX7219(seq, "confirm")
        open_lock(True)
    else:
        runMAX7219(seq, "reject")

    except KeyboardInterrupt:
        open_lock(False)
        pass