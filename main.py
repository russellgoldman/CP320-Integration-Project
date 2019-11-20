import time
import RPi.GPIO as GPIO
from keypad import keypad
from max7219 import display
from infared_sensor import sensor
from servo_motor import lock

GPIO.setwarnings(False)

if __name__ == '__main__':
    correct_seq = []
    digit = input("Enter a digit (-1 to finish): ")
    while digit != "-1":
        if digit == "*" or digit == "#":
            print("%s is not a valid digit" % digit)
        else:
            correct_seq.append(digit)
        digit = input("Enter a digit (-1 to finish): ")
    print(correct_seq)
    print("Accepting readings\n")

    # Initialize
    kp = keypad()
    s = sensor()
    l = lock()
    d = display()

    # check if the infared sensor detects someone
    ok = False
    ok = s.check_reading()

    if not ok:
        d.runMAX7219(None, "too_far")
    else:
        exit = ""
        while exit != "q":
            print("Enter a code: ")
            seq = []
            i = 0
            while i < len(correct_seq):
                digit = None
                while digit == None:
                    digit = kp.getKey()
                if str(digit) == "*":
                    print("Closing lock")
                    l.open_lock(False)
                    kp = keypad()
                else:
                    i += 1
                    seq.append(str(digit))
                print(str(digit))
                time.sleep(0.4)

            # Check digit code
            print(seq)

            if seq == correct_seq:
                print("Code accepted")
                l.open_lock(True)
                d.runMAX7219(seq, "confirm")
            else:
                l.open_lock(False)
                d.runMAX7219(seq, "reject")

            kp = keypad()
            d = display()
            exit = input("Enter q to quit, any other character to continue: ")