import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()
    hsv = cv2.cvtColor(frame , cv2.COLOR_BGR2HSV)

    lower_yellow = np.array([0,0,0])
    upper_yellow = np.array([50,220,240])

    mask = cv2.inRange(hsv, lower_yellow,upper_yellow)
    res = cv2.bitwise_and(frame,frame, mask=mask)

    cv2.imshow('frame',frame)
    cv2.imshow('res',res)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
