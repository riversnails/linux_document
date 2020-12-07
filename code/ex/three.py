import cv2

def main(args):
    
    cap = cv2.VideoCapture(-1)
    st1 = '/usr/local/share/opencv4/haarcascades/haarcascade_frontalface_default.xml'
    face_cascade1=cv2.CascadeClassifier(st1)
    
    st2 = '/usr/local/share/opencv4/haarcascades/haarcascade_eye.xml'
    face_cascade2=cv2.CascadeClassifier(st2)
    
    try:
        while(cap.isOpened()):
            ret, img = cap.read()
            
            if ret:
                gray_img1=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces1=face_cascade1.detectMultiScale(gray_img1, scaleFactor=1.3, minNeighbors=5)
                faces2=face_cascade2.detectMultiScale(gray_img1, scaleFactor=1.3, minNeighbors=5)
                
                for (x,y,w,h) in faces1:
                    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
                    
                for (x,y,w, h) in faces2:
                    cv2.circle(img, (x,y), (w), (0,0,255) , 1)
                
                cv2.imshow('camera-0', img)
                if cv2.waitKey(1) & 0xFF == 27:
                    cv2.imwrite('camera-0.jpg', img)
                    break
            
            else:
                print('no camera')
                break
           
    except KeyboardInterrupt:
        cap.release()
        cv2.destroyAllWindows()
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
