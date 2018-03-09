import numpy as np
import cv2

img = cv2.imread('kohli.jpg',cv2.IMREAD_COLOR)

cv2.line(img, (0,0),(150,150),(0,0,255),10) # args:(img, start, end, color, thickness)
cv2.rectangle(img, (15,20),(350,400),(255,0,0),5) # args:(img, topleft, bottomright, color, thickness)
cv2.circle(img, (150,150),100, (0,255,0), 10) # args:(img, center, radius, color, thickness) thickness of -1 gives filled solid fig

pts = np.array([[100,50],[200,30],[70,200],[500,10]],np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,255,255),5) #args : (img, coord array, True (closed)/False ,color,thickness) 

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(250,350),font,2,(23,3,45),2,cv2.LINE_AA) #args : (img,text,start pos,font,size,color,thickness,line_type)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
