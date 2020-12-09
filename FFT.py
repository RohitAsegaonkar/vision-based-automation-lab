# Author - Rohit Kishor Asegaonkar
# Div-A                Batch - B1
# Roll No.-09         Gr. No.- 11810636 

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Name-FFT(img)
# Inputs - Images
# Description - Returns 2D FFT of input Images.
def FT(img):
    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)
    magnitude_spectrum = 20*np.log(np.abs(fshift))
    return magnitude_spectrum

def IFT(fshift):
    f_ishift = np.fft.ifftshift(fshift)
    img_back = cv2.idft(f_ishift)
    img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])


kernel = np.ones((3,3),np.float32)/9
ms4 = FT(kernel)
img1 = cv2.imread('cameraman.tif',0)
ms1 = FT(img1)

img2 = cv2.imread('line3.png',0)
ms2 = FT(img2)
img3 = cv2.imread('line4.png',0)
ms3 = FT(img3)


plt.subplot(321),plt.imshow(kernel, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(322),plt.imshow(ms4, cmap = 'gray')
plt.title('2D FFt of Image'), plt.xticks([]), plt.yticks([])
plt.subplot(323),plt.imshow(img2, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(324),plt.imshow(ms2, cmap = 'gray')
plt.title('2D FFt of Image'), plt.xticks([]), plt.yticks([])
plt.subplot(325),plt.imshow(img3, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(326),plt.imshow(ms3, cmap = 'gray')
plt.title('2D FFt of Image'), plt.xticks([]), plt.yticks([])
plt.show()

