import numpy as np
import cv2

img = cv2.imread('kohli.jpg', cv2.IMREAD_COLOR)

##img[start:end,start:end]=img[startc:endc,startc:endc]
##start is the first row and end is the last row where the img is to be copied
##startc is the first the row of the image which is to be copied whereas endc is the last row to be copied

##img[start:end,start:end]=-1 uncomment to hollow a region of the image

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
 
##uncomment the desired section
