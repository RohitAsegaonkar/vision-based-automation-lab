# Author - Rohit Kishor Asegaonkar
# Div-A                Batch - B1
# Roll No.-09         Gr. No.- 11810636 

import cv2
import numpy as np
import math
import matplotlib.pyplot as plt 
    
image = cv2.imread('images/spider.jpeg')
image2 = cv2.imread('Results/CameraImage2.png')

kern1 = cv2.getGaborKernel((5, 5), 2.0, 0, 4.0, 0.5, 0, ktype=cv2.CV_64F)
kern2 = cv2.getGaborKernel((5, 5), 2.0, np.pi/4, 4.0, 0.5, 0, ktype=cv2.CV_64F)
kern3 = cv2.getGaborKernel((5, 5), 2.0, np.pi/2, 4.0, 0.5, 0, ktype=cv2.CV_64F)

filtered_img_zero = cv2.filter2D(image,-1,kern1)
filtered_img_fortyfive = cv2.filter2D(image,-1,kern2)
filtered_img_ninety = cv2.filter2D(image,-1,kern3)

res = cv2.add(filtered_img_zero,filtered_img_ninety)
res1 = cv2.add(res,filtered_img_fortyfive)

kern1_test = cv2.getGaborKernel((5, 5), 2.0, 0, 4.0, 0.5, 0, ktype=cv2.CV_64F)
kern2_test = cv2.getGaborKernel((5, 5), 2.0, np.pi/6, 4.0, 0.5, 0, ktype=cv2.CV_64F)
kern3_test = cv2.getGaborKernel((5, 5), 2.0, np.pi/3, 4.0, 0.5, 0, ktype=cv2.CV_64F)

filtered_img_zero_test = cv2.filter2D(image,-1,kern1_test)
filtered_img_fortyfive_test = cv2.filter2D(image,-1,kern2_test)
filtered_img_ninety_test = cv2.filter2D(image,-1,kern3_test)

res_test = cv2.add(filtered_img_zero_test,filtered_img_ninety_test)
res1_test = cv2.add(res_test,filtered_img_fortyfive_test)

error = cv2.norm(res1, res1_test, normType=cv2.NORM_L2)
print(error)

textstr = "Euclidean Distance Between two images is " + str(error)
plt.gcf().text(0.4, 0.1, textstr, fontsize=14)
plt.subplot(131)
plt.title("Original Image")
plt.imshow(image)
plt.subplot(132)
plt.title("Filtered Image")
plt.imshow(res1)
plt.subplot(133)
plt.title("Test Image")
plt.imshow(res1_test)
plt.show()