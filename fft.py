import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('cameraman.tif') # change for your own test image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


dft = cv2.dft(np.float32(gray),flags=cv2.DFT_SCALE | cv2.DFT_REAL_OUTPUT)
dft_shift = np.fft.fftshift(dft)
f_ishift = np.fft.ifftshift(dft_shift)
img_back = cv2.idft(f_ishift, flags=cv2.DFT_SCALE | cv2.DFT_REAL_OUTPUT)
img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])

print (img_back.max(), img_back.min()) # too large!!!!

plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img_back, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()