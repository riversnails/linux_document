#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np

def onControl(pos):
	global img, height, width
	rotate = cv2.getTrackbarPos('rotate', 'main')
	scale = cv2.getTrackbarPos('scale', 'main')
	matrix=cv2.getRotationMatrix2D((width/2, height/2), rotate, scale)
	dst=cv2.warpAffine(img, matrix, (width, height))
	cv2.imshow('main', dst)
	#print(f"rotate={rotate}")


img=cv2.imread("IMG/sta.jpeg", cv2.IMREAD_COLOR)
height, width, channel=img.shape
img=cv2.resize(img, (width*2, height*2), interpolation=cv2.INTER_LANCZOS4)
height, width, channel=img.shape

print(img.ndim)
print(img.shape)
print(img.dtype)

img2=img.reshape(-1, img.shape[0] , img.shape[1])

print(img2.ndim)
print(img2.shape)
print(img2.dtype)

img3=img.flatten()

print(img3.ndim)
print(img3.shape)
print(img3.dtype)

img4=img.copy()

img4[10:50,10:50,0] = 255
img4[10:50,60:100,1] = 255
img4[10:50,110:150,2] = 255


cv2.imshow('main',img)
cv2.imshow('test',img4)
cv2.createTrackbar('rotate', 'main', 0, 360, onControl)
cv2.createTrackbar('scale', 'main', 1, 100, onControl)

'''
img2 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
img3 = cv2.rotate(img, cv2.ROTATE_180)
img4 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

cv2.imshow('2',img2)
cv2.imshow('3',img3)
cv2.imshow('4',img4)

matrix=cv2.getRotationMatrix2D((width/2, height/2), 125, 1.1)
dst=cv2.warpAffine(img, matrix, (width, height))
cv2.imshow('matrix', dst)
'''

while True:
	key = cv2.waitKeyEx(30)
	#print(key)
	if key == 0x1B:
		break
	elif key == ord('1'):
		img=cv2.flip(img, 0)
		cv2.imshow('main',img)
	elif key == ord('2'):
		img=cv2.flip(img, 1)
		cv2.imshow('main',img)
	elif key == ord('3'):
		img=cv2.flip(img, -1)
		cv2.imshow('main',img)
		

cv2.destroyAllWindows()
