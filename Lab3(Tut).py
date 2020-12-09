# Author - Rohit Kishor Asegaonkar
# Div-A                Batch - B1
# Roll No.-09         Gr. No.- 11810636 

import cv2 
import numpy as np 
import matplotlib.pyplot as plt 
   
# Read an image 
image = cv2.imread('cameraman.tif') 
   
# Apply log transformation method 
c = 255 / np.log(1 + np.max(image))
log_image =  c * (np.log(image + 1)) 
   
# float value will be converted to int 
log_image = np.array(log_image, dtype = np.uint8) 
   
# Plotting Histogram 
hist,bins = np.histogram(image.flatten(),256,[0,256])
hist,bins = np.histogram(log_image.flatten(),256,[0,256])

# show the plotting graph of an image  
plt.figure(1)
plt.subplot(221)
plt.title("Raw Image")
plt.imshow(image)
plt.subplot(222)
plt.title("Log-Transformed Image")
plt.imshow(log_image)
plt.subplot(223)
plt.title("Histogram of Raw Image")
plt.hist(image.flatten(),256,[0,256], color = 'c')
plt.xlim([0,256])
plt.legend(('histogram'), loc = 'upper left')
plt.subplot(224)
plt.title("Histogram of Log-Transform Image")
plt.hist(log_image.flatten(),256,[0,256], color = 'm')
plt.xlim([0,256])
plt.legend(('histogram'), loc = 'best')
plt.show()
