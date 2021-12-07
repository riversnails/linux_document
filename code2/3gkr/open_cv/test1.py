#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np

img=np.full((500,500,3), 255, dtype=np.uint8)
cv2.imshow('img',img)
img2=np.full((500,500,3), 0, dtype=np.uint8)
cv2.imshow('img2',img2)
img3=np.zeros((500,500,3), dtype=np.uint8)+255
cv2.imshow('img3',img3)


cv2.waitKey()
cv2.destroyAllWindows()
