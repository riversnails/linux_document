import RPi.GPIO as g
import picamera as camera
import time

ECHO = 16
TRIG = 20

def get_distance():
    g.output(TRIG, g.LOW)
    time.sleep(0.5)
    g.output(TRIG, g.HIGH)
    time.sleep(0.0001)
    g.output(TRIG, g.LOW)
    
    while g.input(ECHO) == g.LOW:
        pulse_begin = time.time()
    
    while g.input(ECHO) == g.HIGH:
        pulse_end = time.time()
    
    duration = float(pulse_end - pulse_begin)
    distance = (340 * (duration/2)) * 100
    return distance

def main(args):
    g.setmode(g.BCM)
    
    g.setup(ECHO, g.IN)
    g.setup(TRIG, g.OUT)
    g.output(TRIG, g.LOW)
    i = 0
    try:
        while True:    
            if get_distance() < 10:
                print(i)
                cam = camera.PiCamera()
                cam.start_preview()
                time.sleep(3)
                cam.capture("/home/pi/cam{:03}.jpg".format(i))
                i+=1
                cam.stop_preview()
                cam.close()
            time.sleep(1)
    except KeyboardInterrupt:
        g.cleanup()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
