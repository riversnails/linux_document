#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np

def onControl(pos):
	global img
	r = cv2.getTrackbarPos('R', 'img')
	g = cv2.getTrackbarPos('G', 'img')
	b = cv2.getTrackbarPos('B', 'img')
	
	img[:]=(b,g,r)
	cv2.imshow('img',img)
	print(f"r={r}, g={g}, b={b}")


x_direction = 250
y_direction = 250
toggle = 0

img=np.full((500,500,3), 0, dtype=np.uint8)
cv2.imshow('img',img)
cv2.createTrackbar('R', 'img', 0, 255, onControl)
cv2.createTrackbar('G', 'img', 0, 255, onControl)
cv2.createTrackbar('B', 'img', 0, 255, onControl)



cv2.waitKey()
cv2.destroyAllWindows()
