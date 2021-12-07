import picamera as camera
import time

def main(args):
    cam = camera.PiCamera()
    cam.start_preview()
    cam.start_recording("/home/pi/video01.h264")
    cam.wait_recording(5)
    cam.stop_preview()
    cam.stop_recording()
    cam.close()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))