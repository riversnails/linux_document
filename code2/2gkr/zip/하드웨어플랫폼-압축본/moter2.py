import RPi.GPIO as GPIO
import time

PUSH_PIN = 17
PUSH_PIN2 = 16
IN_A = 21
IN_B = 20

def moterStop():
    moterPWM.ChangeDutyCycle(0)
        
def moterStart(moterPWM):
    moterPWM.ChangeDutyCycle(30)
    print("Duty : {0}", format(30))
        
def main(args):
    toggle = 0
    toggle2 = 0
    toggle3 = 0
    
    GPIO.setmode(GPIO.BCM)
    
    GPIO.setup(IN_A, GPIO.OUT)
    GPIO.setup(IN_B, GPIO.OUT)
    
    GPIO.setup(PUSH_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.setup(PUSH_PIN2, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    
    
    try:
        while True:
            if GPIO.input(PUSH_PIN) == GPIO.LOW :
                if toggle == 1:
                    toggle = 0
                    if toggle3 == 0:
                        toggle3 = 1
                        GPIO.output(IN_A, GPIO.HIGH)
                        GPIO.output(IN_B, GPIO.LOW)
                    else:
                        toggle3 = 0
                        GPIO.output(IN_A, GPIO.LOW)
                        GPIO.output(IN_B, GPIO.HIGH)
                        
            else:
                if toggle == 0:
                    toggle = 1
                    print("Push UP")
                
            if GPIO.input(PUSH_PIN2) == GPIO.LOW :
                if toggle2 == 1:
                    toggle = 0
                    GPIO.output(IN_A, GPIO.LOW)
                    GPIO.output(IN_B, GPIO.LOW)
                    
            else:
                if toggle2 == 0:
                    toggle2 = 1
                    
            time.sleep(0.1)
    except KeyboardInterrupt:
        GPIO.cleanup()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

