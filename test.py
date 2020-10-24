import cv2
import numpy as np

I = cv2.imread('data/lenna.png')
# cv2.imshow('lenna', I)
# cv2.waitKey(0)

len, width, channels = I.shape
print((len, width, channels))

I = I.reshape(len * width * channels)
print(I)
