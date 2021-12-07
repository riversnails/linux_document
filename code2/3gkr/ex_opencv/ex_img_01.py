'''
import cv2

image = cv2.imread("IMG/sta.jpeg", cv2.IMREAD_COLOR)


h,w,c = image.shape

print(f"HEIGHT={h}, WEIGHT={w}, CHANNEL-{c}")

cv2.imshow("STA", image)

key=cv2.waitKey(1000)
print(key)

cv2.destroyAllWindows()
'''

import cv2

image = cv2.imread("IMG/rain.png", cv2.IMREAD_COLOR)
image2 = cv2.imread("IMG/rain.png", cv2.IMREAD_GRAYSCALE)


h,w = image2.shape

print(f"HEIGHT={h}, WEIGHT={w}")

cv2.imshow("STA", image2)

key=cv2.waitKey(1000)
print(key)


if key == ord('g'):
	cv2.imwrite(f"IMG/img_gray_copy.jpg", image2)
elif key == 115:
	cv2.imwrite(f"IMG/img_color_copy.jpg", image)
	

cv2.destroyAllWindows()
