# Author - Rohit Kishor Asegaonkar
# Div-A                Batch - B1
# Roll No.-09         Gr. No.- 11810636 

import cv2
import numpy as np
import matplotlib.pyplot as plt 

f = 0.25
sigma_x = sigma_y = 4.0
theta = np.pi/2
image = cv2.imread('saturn.png')

gabor_kernel = np.zeros((7,7))

for x in range(-3,3,1):
    for y in range(-3,3,1):
        x2 = x * np.cos(theta) + y * np.sin(theta)
        y2 = x * np.cos(theta) - y * np.sin(theta)
        gabor_kernel[x,y] = (np.exp(-1/2 * ((x2**2/sigma_x**2)+ (y2**2/sigma_y**2)))) * (np.cos(2*np.pi*f*x2))

print(gabor_kernel)
