"""
import cv2

def main(args):
    file = 'download.jpg'
    img = cv2.imread(file, cv2.IMREAD_COLOR)
    
    cv2.imshow('Our Comrade Stalin', img)
    k = cv2.waitKey(0)
    
    if k == 27:
        cv2.destroyAllWindows()
    elif k == ord('s'):
        cv2.imwrite('output.png', img)
        cv2.destroyAllWindows()
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
"""

"""
import cv2

def main(args):
    
    cap = cv2.VideoCapture(-1)
    
    while(cap.isOpened()):
        ret, img = cap.read()
        
        if ret:
            cv2.imshow('camera-0', img)
            
            if cv2.waitKey(1) & 0xFF == 27:
                cv2.imwrite('camera-0.jpg', img)
                break
        
        else:
            print('no camera')
            break
            
    cap.release()
    cv2.destroyAllWindows()
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
"""

"""
import cv2
import numpy as np

def main(args):
    
    img = np.zeros((512,512,3), np.uint8)
    
    img = cv2.line(img, (0,0), (0,5) , 5)
    img = cv2.rectangle(img, (384,0), (510,128),(0,255,0) , 3)
    img = cv2.circle(img, (477,63), 63, (0,0,255) , -1)
    img = cv2.ellipse(img, (256,256), (100,50) , 0,0,180,(255,0,0),-1)
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, 'hello Cv', (10, 500), font, 2, (255,255,255), 2, cv2.LINE_AA)
    
    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
"""

"""
import cv2
import numpy as np

def main(args):
    
    img = cv2.imread('people.jpeg')
    st = '/usr/local/share/opencv4/haarcascades/haarcascade_frontalface_default.xml'
    face_cascade=cv2.CascadeClassifier(st)
    gray_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    faces=face_cascade.detectMultiScale(gray_img, scaleFactor=1.3, minNeighbors=5)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
        
    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
"""

"""
import cv2

def main(args):
    
    cap = cv2.VideoCapture(-1)
    st = '/usr/local/share/opencv4/haarcascades/haarcascade_frontalface_default.xml'
    face_cascade=cv2.CascadeClassifier(st)
    
    while(cap.isOpened()):
        ret, img = cap.read()
        
        if ret:
            gray_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces=face_cascade.detectMultiScale(gray_img, scaleFactor=1.3, minNeighbors=5)
            for (x,y,w,h) in faces:
                cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
                
            cv2.imshow('camera-0', img)
            
            if cv2.waitKey(1) & 0xFF == 27:
                cv2.imwrite('camera-0.jpg', img)
                break
        
        else:
            print('no camera')
            break
            
    cap.release()
    cv2.destroyAllWindows()
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
"""

"""
from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(5)
camera.capture('/home/pi/image.jpg')
camera.stop_preview()
"""
