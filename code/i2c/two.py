import time
import RPi_I2C_driver as i2c
import RPi.GPIO as GPIO
import picamera as camera

TRIG_PIN = 24
ECHO_PIN = 23

def main(args):
    # 초기화
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRIG_PIN, GPIO.OUT)
    GPIO.setup(ECHO_PIN, GPIO.IN)
    GPIO.setup(TRIG_PIN, GPIO.LOW)
    cam = camera.PiCamera()
    toggle = 0
    i = 1
    while True:
        GPIO.output(TRIG_PIN, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(TRIG_PIN, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(TRIG_PIN, GPIO.LOW)
        
        while GPIO.input(ECHO_PIN) == GPIO.LOW:
            pulse_begin=time.time()
            
        while GPIO.input(ECHO_PIN) == GPIO.HIGH:
            pulse_end=time.time()
            
        duration = float(pulse_end - pulse_begin)
        distance = (340 * (duration/2) ) * 100;
        print(distance)
        if(distance <= 15 and toggle == 0):
            toggle = 1
            cam.start_preview()
            cam.start_recording("/home/pi/video0{0}.h264".format(i))
            
        elif(distance >= 15 and toggle == 1):
            toggle = 0
            cam.stop_preview()
            cam.stop_recording()
            i+=1
        time.sleep(1)
    
    return 0
    
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
    
    
