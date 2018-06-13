##All the moving objects will be displayed here
##This is better to be called as no-action reduction than background reduction
import cv2
import numpy as np

cap = cv2.VideoCapture(0) ##You can either use the cam or enter your video address here. 
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)

    cv2.imshow('original', frame)
    cv2.imshow('fg', fgmask)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
