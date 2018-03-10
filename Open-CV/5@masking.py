import cv2
import numpy as mp

##read the images
img=cv2.imread('kohli.jpg')
logo=cv2.imread('logo1.jpg')

##get the size of the logo
rows,cols,channels=logo.shape
##get the region of interest
roi=img[0:rows,0:cols]

##creating the masks
img2gray=cv2.cvtColor(logo,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray,200,250,cv2.THRESH_BINARY_INV)#mask
mask_inv=cv2.bitwise_not(mask)#inverse of the mask which is to be applied to the roi

fg=cv2.bitwise_and(logo,logo,mask=mask)
bg=cv2.bitwise_and(roi,roi,mask=mask_inv)
final=cv2.add(fg,bg)#modification needed in the roi of the image

img[0:rows,0:cols]=final#modification

cv2.imshow('img2gray',img2gray)
cv2.imshow('mask',mask)
cv2.imshow('mask_inv',mask_inv)
cv2.imshow('fg',fg)
cv2.imshow('bg',bg)
cv2.imshow('final',final)
cv2.imshow('img',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
