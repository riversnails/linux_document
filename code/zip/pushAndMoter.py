import RPi.GPIO as GPIO
import time

PUSH_PIN = 17

def main(args):
    GPIO.setmode(GPIO.BCM)
    
    GPIO.setup(PUSH_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    
    try:
        while True:
            if GPIO.input(PUSH_PIN) == GPIO.LOW :
                print("Push DOWN")
            else:
                print("Push UP")
            time.sleep(0.1)
    except KeyboardInterrupt:
        GPIO.cleanup()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
