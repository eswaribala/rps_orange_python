# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 22:41:26 2017

@author: BALASUBRAMANIAM
"""
import sys
import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import imread, imsave
#sys.path.append("C:/Users/BALASUBRAMANIAM/Pictures/")
image_data = imread('C:/Users/BALASUBRAMANIAM/Pictures/changedata.jpg').astype(np.float32)
print(image_data)

print ('Size: ', image_data.size)
print ('Shape: ', image_data.shape)
scaled_image_data = image_data / 255
#Save the modified image if you want to
imsave('test_out.png', scaled_image_data)
plt.imshow(image_data)
plt.show()

