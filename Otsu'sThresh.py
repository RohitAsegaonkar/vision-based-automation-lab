import numpy as np
import skimage.color
import skimage.filters
import skimage.io
import skimage.viewer


# read and display the original image
image = skimage.io.imread('coins.png')
viewer = skimage.viewer.ImageViewer(image)
viewer.show()

# blur and grayscale before thresholding
blur = skimage.color.rgb2gray(image)
blur = skimage.filters.gaussian(image, sigma=sigma)

# perform adaptive thresholding
t = skimage.filters.threshold_otsu(blur)
mask = blur > t

viewer = skimage.viewer.ImageViewer(mask)
viewer.show()

# use the mask to select the "interesting" part of the image
sel = np.zeros_like(image)
sel[mask] = image[mask]

# display the result
viewer = skimage.viewer.ImageViewer(sel)
viewer.show()