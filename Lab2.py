# Author - Rohit Kishor Asegaonkar
# Div-A                Batch - B1
# Roll No.-09         Gr. No.- 11810636 

import cv2 
import numpy as np 
import matplotlib.pyplot as plt 
   
# Read an image 
image = cv2.imread('pout.tif') 
   
# Apply log transformation method 
c = 180
log_image = c * (np.log(image + 1)) 
   
# float value will be converted to int 
log_image = np.array(log_image, dtype = np.uint8) 
   
plt.figure(1)
plt.subplot(211)
plt.title("Raw Image")
plt.imshow(image)
plt.subplot(212)
plt.title("Log-Transformed Image")
plt.imshow(log_image)
plt.show()