#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np

p_x = -1
p_y = -1
draw_toggle = 0
r = 0
g = 0
b = 0
line = 1
draw_type = 1
img=np.full((500,500,3), 255, dtype=np.uint8)

def onControl(pos):
	global img, r, g, b, line
	r = cv2.getTrackbarPos('R', 'my canvas')
	g = cv2.getTrackbarPos('G', 'my canvas')
	b = cv2.getTrackbarPos('B', 'my canvas')
	line = cv2.getTrackbarPos('LINE', 'my canvas')
	
	if line == 0:
		line = 1
		cv2.createTrackbar('LINE', 'my canvas', 1, 100, onControl)
		
	
	print(f"r={r}, g={g}, b={b} line={line}")

def onMouse(event, x, y, flags, param):
	global img, draw_toggle, r, g, b, p_x, p_y, line, draw_type
	if event == cv2.EVENT_LBUTTONDOWN:
		print("LBTN DOWN", x, y)
		draw_toggle = 1
		if p_x == -1 and p_y == -1:
			p_x = x
			p_y = y
	elif event == cv2.EVENT_MOUSEMOVE and draw_toggle == 1:
		
		print("LBTN DOWN&DRAW", x, y, p_x, p_y)
		
		if draw_type == 1:
			cv2.line(img, (x, y), (p_x, p_y), (b, g, r), line)
			cv2.imshow('my canvas', img)
			p_x = x
			p_y = y
		
	elif event == cv2.EVENT_LBUTTONUP:
		print("LBTN UP", x, y)
		draw_toggle = 0;
		if draw_type == 2:
			cv2.rectangle(img, (x, y), (p_x, p_y), (b, g, r), line)
			cv2.imshow('my canvas', img)
		elif draw_type == 3:
			cv2.circle(img, ( (int)((x-p_x)/2 + p_x), (int)((y-p_y)/2 + p_y) ), 50, (b, g, r), line)
			#cv2.ellipse(img, ((int)((x-p_x)/2 + p_x),(int)((y-p_y)/2 + p_y)), (p_x, y), 0, 0, 180, (b, g, r), line)
			cv2.imshow('my canvas', img)
			
		p_x = -1
		p_y = -1


cv2.imshow('my canvas',img)
cv2.createTrackbar('R', 'my canvas', 0, 255, onControl)
cv2.createTrackbar('G', 'my canvas', 0, 255, onControl)
cv2.createTrackbar('B', 'my canvas', 0, 255, onControl)
cv2.createTrackbar('LINE', 'my canvas', 1, 100, onControl)
cv2.setMouseCallback('my canvas', onMouse, [img])


while True:
	key = cv2.waitKey()
	if key == ord('s'):
		cv2.imwrite('save.jpg', img)
		break
	elif key == ord('1'):
		draw_type = 1
	elif key == ord('2'):
		draw_type = 2
	elif key == ord('3'):
		draw_type = 3
	elif key == 0x1B:
		break
		
		

cv2.destroyAllWindows()
