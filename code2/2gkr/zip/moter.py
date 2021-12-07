import RPi.GPIO as GPIO
import time

IN_A = 21
IN_B = 20

def moterControl(moterPWMA, moterPWMB):
    for i in range(0, 50):
        moterPWMA.ChangeDutyCycle(i)
        print("Duty : {0}", format(i))
        time.sleep(0.07)
                
    for i in range(0, 50):
        moterPWMB.ChangeDutyCycle(i)
        print("Duty : {0}", format(i))
        time.sleep(0.07)
            
    for i in range(0, 50):
        time.sleep(0.07)

def main(args):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(IN_A, GPIO.OUT)
    GPIO.setup(IN_B, GPIO.OUT)
    
    moterPWMA = GPIO.PWM(IN_A, 50)
    moterPWMA.start(0)
    
    moterPWMB = GPIO.PWM(IN_B, 50)
    moterPWMB.start(0)
    
    try:
        while True:
            moterControl(moterPWMA, moterPWMB)
    
    except KeyboardInterrupt:
        GPIO.cleanup()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))