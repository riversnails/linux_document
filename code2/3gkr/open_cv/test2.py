#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np

def onMouse(event, x, y, flags, param):
	global img
	if event == cv2.EVENT_LBUTTONDOWN:
		print("LBTN Click", x, y)
		cv2.rectangle(img, (x - 50, y - 50), (x + 50, y + 50), (255, 0, 0), 2)
		cv2.imshow(' my canvas ',img)
	elif event == cv2.EVENT_RBUTTONDOWN:
		print("RBTN Click", x, y)
		cv2.circle(img, (x, y), 50, (0, 255, 0), 2)
		cv2.imshow(' my canvas ',img)
	elif event == cv2.EVENT_LBUTTONDBLCLK:
		print("L Double Click", x, y)
		img=np.full((500,500,3), 255, dtype=np.uint8)
		cv2.imshow(' my canvas ',img)
	elif event == cv2.EVENT_RBUTTONDBLCLK:
		print("R Double Click", x, y)

x_direction = 250
y_direction = 250
toggle = 0

img=np.full((500,500,3), 255, dtype=np.uint8)
cv2.circle(img, (x_direction, y_direction), 50, (0, 255, 0), 2)
cv2.imshow(' my canvas ',img)

cv2.setMouseCallback(' my canvas ', onMouse, [img])

while True:
	key = cv2.waitKeyEx(30)
	#print(key)
	if key == 0x1B:
		break
	elif key == 0xff53:
		toggle = 1
		x_direction = x_direction + 1
		print("R")
	elif key == 0xff54:
		toggle = 1
		y_direction = y_direction + 1
		print("D")
	elif key == 0xff51:
		toggle = 1
		x_direction = x_direction - 1
		print("L")
	elif key == 0xff52:
		toggle = 1
		y_direction = y_direction - 1
		print("U")
		
	if toggle == 1:
		toggle = 0
		img=np.full((500,500,3), 255, dtype=np.uint8)
		cv2.circle(img, (x_direction, y_direction), 50, (0, 255, 0), 2)
		cv2.imshow(' my canvas ',img)

cv2.line(img, (10, 10), (50, 50), (0, 0, 255), 3)
cv2.rectangle(img, (50, 50), (250, 250), (255, 0, 0), 2)
cv2.circle(img, (300, 300), 50, (0, 255, 0), 2)
cv2.putText(img, "asdf",  (100, 100), cv2.FONT_HERSHEY_COMPLEX, 3, (0, 255, 0), 2)


cv2.destroyAllWindows()
