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
import time

WIN_NAME = "image"

image = cv2.imread("IMG/rain.png", cv2.IMREAD_COLOR)
#image2 = cv2.imread("IMG/sta.jpeg", cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread("IMG/sta.jpeg", cv2.IMREAD_COLOR)


h,w,c = image2.shape

print(f"HEIGHT={h}, WEIGHT={w}")

#cv2.namedWindow(WIN_NAME, cv2.WINDOW_NORMAL)
#cv2.setWindowProperty(WIN_NAME, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

str1 = "Stalin!"
str2 = f"HEIGHT={h}, WEIGHT={w}, CHANNEL-{c}"

image3=cv2.resize(image2, None, fx=2, fy=2)
cv2.putText(image3, str1, (0, 200), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 0.7, (255, 0, 0))
cv2.putText(image3, str2, (0, 230), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 0.5, (255, 0, 0))
#cv2.resizeWindow(WIN_NAME, 400, 800)
#cv2.imshow(WIN_NAME, image3)
cv2.imshow("image", image2)

size = 1
check = True

while check:

	key=cv2.waitKey(5000)
	print(key)

	if key == ord('g'):
		cv2.imwrite(f"IMG/img_gray_copy.jpg", image1)
	elif key == ord('c'):
		cv2.imwrite(f"IMG/img_color_copy.jpg", image1)
	elif key == ord('u'):
		if size < 5:
			size = size + 0.1
		image3=cv2.resize(image2, None, fx=size, fy=size)
		cv2.imshow("image", image3)
	elif key == ord('d'):
		if size > 0.2:
			size = size - 0.1
		image3=cv2.resize(image2, None, fx=size, fy=size)
		cv2.imshow("image", image3)
	elif key == ord('q'):
		cv2.destroyAllWindows()
		check = False
		



'''
if key == ord('g'):
	cv2.imwrite(f"IMG/img_gray_copy.jpg", image1)
elif key == ord('c'):
	cv2.imwrite(f"IMG/img_color_copy.jpg", image1)
elif key == ord('u'):
	image3=cv2.resize(image2, None, fx=2, fy=2)
	cv2.imwrite(f"IMG/img_color_copy.jpg", image3)
elif key == ord('d'):
	image3=cv2.resize(image2, None, fx=0.5, fy=0.5)
	cv2.imwrite(f"IMG/img_color_copy.jpg", image3)
elif key == ord('q'):
	cv2.destroyAllWindows()
'''
	

cv2.destroyAllWindows()

