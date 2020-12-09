# Author - Rohit Kishor Asegaonkar
# Div-A                Batch - B1
# Roll No.-09         Gr. No.- 11810636 

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/coins.png',0)

# global thresholding
ret1,th1 = cv2.threshold(img,84,255,cv2.THRESH_TOZERO)

# Otsu's thresholding
ret2,th2 = cv2.threshold(img,0,255,cv2.THRESH_TOZERO+cv2.THRESH_OTSU)

# plot all the images and their histograms
images = [img, 0, th1,
          img, 0, th2,]
titles = ['Original Noisy Image','Histogram','Global Thresholding (v=84)',
          'Original Noisy Image','Histogram',"Otsu's Thresholding"]

for i in range(2):
    plt.subplot(2,3,i*3+1),plt.imshow(images[i*3],'gray')
    plt.title(titles[i*3]), plt.xticks([]), plt.yticks([])
    plt.subplot(2,3,i*3+2),plt.hist(images[i*3].ravel(),256)
    plt.title(titles[i*3+1]), plt.xticks([]), plt.yticks([])
    plt.subplot(2,3,i*3+3),plt.imshow(images[i*3+2],'gray')
    plt.title(titles[i*3+2]), plt.xticks([]), plt.yticks([])
plt.show()