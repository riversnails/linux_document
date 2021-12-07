import RPi.GPIO as GPIO
import picamera as camera
import time

PUSH_PIN = 21
toggle = 0

def main(args):
    
    

    GPIO.setmode(GPIO.BCM)
    
    GPIO.setup(PUSH_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    
    try:
        global toggle
        while True:
            if GPIO.input(PUSH_PIN) == GPIO.LOW :
                if toggle == 1:
                    toggle = 0
                    print("DOWN")
                    cam = camera.PiCamera()
                    cam.start_preview()
                    time.sleep(3)
                    cam.capture("/home/pi/cam011.jpg")
                    cam.stop_preview()
                    cam.close()
            
            else:
                if toggle == 0:
                    toggle = 1
                    print("UP")
                    
            time.sleep(0.1)
    except KeyboardInterrupt:
        GPIO.cleanup()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
