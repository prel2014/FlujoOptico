import numpy as np
import cv2

cap = cv2.VideoCapture(1)
imgs = list()
kernel = np.zeros((3,3),np.float32)
kernel[0,0]=1.0
kernel[0,2]=1.0
kernel[2,0]=1.0
kernel[2,2]=1.0
while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    imgs.append(gray[:,:,1])
    #print(imgs[0].shape)
    flujo = np.zeros((gray.shape[0],gray.shape[1]))
    if len(imgs)==2:
        flujo = imgs[1]/255.0 - imgs[0]/255.0
        #flujo = cv2.filter2D(flujo/255.0,-1,kernel)
        imgs=list()
    cv2.imshow('frame2',flujo)    
    cv2.imshow('frame1',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
