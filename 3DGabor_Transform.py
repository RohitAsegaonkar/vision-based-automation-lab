# Author - Rohit Kishor Asegaonkar
# Div-A                Batch - B1
# Roll No.-09         Gr. No.- 11810636 

import numpy as np
import argparse
import cv2
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm


sigma = 25
[X, Y] = np.meshgrid(np.arange(-100, 101), np.arange(-100, 101))
Z = 1/(np.sqrt(2.0 * np.pi) * sigma) * np.exp(-(X**2+Y**2)/(2.0*sigma**2))

dx = np.roll(Z, 1, axis=1) - Z
dx2 = np.roll(dx, 1, axis=1) - dx

dy = np.roll(Z, 1, axis=0) - Z
dy2 = np.roll(dy, 1, axis=0) - dy

LoG = -(dx2+dy2)

fig = plt.figure()
ax = fig.add_subplot(131, projection='3d')
plt.title("Gaussian")
ax.plot_surface(X, Y, Z,cmap=cm.PiYG)

ax = fig.add_subplot(132, projection='3d')
plt.title("First order derivative")
ax.plot_surface(X, Y, dx + dy,cmap=cm.cubehelix)

ax = fig.add_subplot(133, projection='3d')
plt.title("Second order derivative (Laplacian of Gaussian)")
ax.plot_surface(X, Y, LoG,cmap=cm.coolwarm)
plt.show()