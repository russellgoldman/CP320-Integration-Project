import time
import RPi.GPIO as GPIO
from keypad import keypad
 
GPIO.setwarnings(False)
 
if __name__ == '__main__':
    # Initialize
    kp = keypad()
 
    ###### 4 Digit wait ######
    seq = []
    for i in range(4):
        digit = None
        while digit == None:
            digit = kp.getKey()
            print(digit)
        seq.append(digit)
        time.sleep(0.4)
 
    # Check digit code
    print(seq)
    if seq == [1, 2, 3, '#']:
        print("Code accepted")