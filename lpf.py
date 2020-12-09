# Author - Rohit Kishor Asegaonkar
# Div-A                Batch - B1
# Roll No.-09         Gr. No.- 11810636 

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/cameraman.tif')

kernel = np.ones((3,3),np.float32)/9
dst = cv2.filter2D(img,-1,kernel)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()