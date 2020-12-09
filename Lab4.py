# Author - Rohit Kishor Asegaonkar
# Div-A                Batch - B1
# Roll No.-09         Gr. No.- 11810636 

import cv2 
import numpy as np 
import matplotlib.pyplot as plt 
   
# Read an image 
image = cv2.imread('images/cameraman.tif')

sobelx = cv2.Sobel(image,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(image,cv2.CV_64F,0,1,ksize=5)

plt.subplot(321),plt.imshow(image,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(322),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(323),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])


f = np.fft.fft2(image)
fshift1 = np.fft.fftshift(f)
magnitude_spectrum1 = 20*np.log(np.abs(fshift1))


gx = np.fft.fft2(sobelx)
fshift2 = np.fft.fftshift(gx)
magnitude_spectrum2 = 20*np.log(np.abs(fshift2))



#a = cv2.multiply(f, gx)
#
#img_back = np.fft.ifft2(a)
#
#img_back = np.abs(img_back)

plt.subplot(324),plt.imshow(magnitude_spectrum1, cmap = 'gray')
plt.title('Magnitude Spectrum Image'), plt.xticks([]), plt.yticks([])
plt.subplot(325),plt.imshow(magnitude_spectrum2, cmap = 'gray')
plt.title('Magnitude Spectrum Gx'), plt.xticks([]), plt.yticks([])
#plt.subplot(326),plt.imshow(img_back, cmap = 'gray')
#plt.title('Image after FFt'), plt.xticks([]), plt.yticks([])
plt.show()