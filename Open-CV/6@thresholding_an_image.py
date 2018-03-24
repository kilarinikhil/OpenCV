import cv2
import numpy as np

img=cv2.imread('bookpage.jpg')

retval1,threshold1=cv2.threshold(img,12,255,cv2.THRESH_BINARY)

grayscaled=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#conversion to grayscale

retval2,threshold2=cv2.threshold(grayscaled,10,255,cv2.THRESH_BINARY)#thresholding the grayscaled image

gauss=cv2.adaptiveThreshold(grayscaled,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
##for other types of filters refer the documentation

cv2.imshow('actual',img)
cv2.imshow('threshold1',threshold1)
##cv2.imshow('threshold2',threshold2)
cv2.imshow('gauss',gauss)
 ##cv2.imshow('grayscaled',grayscaled)
cv2.waitKey(0)
cv2.destroyAllWindows()
