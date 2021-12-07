import RPi.GPIO as GPIO
import time

R_LED_PIN  = 16
G_LED_PIN  = 20
B_LED_PIN  = 21

def main(args):

    GPIO.setmode(GPIO.BCM)
    
    GPIO.setup(R_LED_PIN, GPIO.OUT)
    
    GPIO.output(R_LED_PIN, GPIO.OUT)
    time.sleep(1)
    GPIO.output(R_LED_PIN, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(R_LED_PIN, GPIO.OUT)
    time.sleep(1)
    GPIO.output(R_LED_PIN, GPIO.HIGH)
    time.sleep(1)
    
if __name__ == '__main__':
    import sys
    
    sys.exit(main(sys.argv))