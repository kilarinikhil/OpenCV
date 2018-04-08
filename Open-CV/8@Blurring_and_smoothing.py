import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0,0,0])
    upper_red = np.array([50,220,240])#Defining the upper limits for lemon yellow

    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask = mask)

    kernel = np.ones((15,15),np.float32)/225#Defining the filter
    smoothed = cv2.filter2D(res,-1,kernel)#Applying the filter

    #Gaussian Blur
    blur = cv2.GaussianBlur(res, (15,15),0) 

    #Median Blur
    median = cv2.medianBlur(res,15)

    #Bilateral Blur
    bilateral = cv2.bilateralFilter(res,15,75,75)
    
    cv2.imshow('frame', frame)#The actual feed to the camera
    ##Uncommen the desired output among all the median filter is the best.
    ##cv2.imshow('mask', mask)
    ##cv2.imshow('res', res)
    ##cv2.imshow('smoothed', smoothed)
    ##cv2.imshow('blur', blur)
    ##cv2.imshow('median', median)
    cv2.imshow('bilateral', bilateral)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
