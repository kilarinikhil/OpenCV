import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('kohli.jpg',cv2.IMREAD_GRAYSCALE)
##picture is available in the folder

##cv2.imshow("image",img)
##cv2.waitKey(0)
##cv2.destroyAllWindows()
##You can either use this section by commenting the bottom section if you prefer cv2 library

plt.imshow(img ,cmap = 'c',interpolation = 'bicubic')
plt.show()
