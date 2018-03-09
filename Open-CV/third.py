import numpy as np
import cv2

img = cv2.imread('kohli.jpg', cv2.IMREAD_COLOR)

pts=np.array([[20,5],[20,20],[30,20],[30,5]],np.int32)

cv2.polylines(img,[pts],True,(30,30,30),2)

font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'KING KOHLI!',(200,200),font,1,(70,70,70),2,cv2.LINE_AA)

cv2.imshow('kohli',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
 
