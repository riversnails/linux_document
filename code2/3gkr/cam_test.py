#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import picamera as camera
import time

def main(args):
	cam=camera.PiCamera()
	cam.resolution = (640, 480)
	cam.start_preview()
	time.sleep(1)
	
	
	cam.capture("/home/pi/Pictures/asdf.jpg")
	cam.stop_preview()
	print("end")
	cam.close()
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
