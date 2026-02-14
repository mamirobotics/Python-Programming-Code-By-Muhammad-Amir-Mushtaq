import cv2
import numpy as np
import matplotlib.pyplot as plt

A = np.zeros((128,256,3))

# Yellow
A[0:63,0:63,1] = 255 
A[0:63,0:63,2] = 255 
# White
A[0:63,64:127,0] = 255
A[0:63,64:127,1] = 255
A[0:63,64:127,2] = 255
# Magenta
A[0:63,128:191,0] = 255
A[0:63,128:191,2] = 255

# Red
A[0:63,192:255,2] = 255

# Green
A[64:127,0:63,1] = 255

# Cyan
A[64:127,64:127,0] = 255
A[64:127,64:127,1] = 255

# Blue
A[64:127,128:191,0] = 255


cv2.imshow("image", A)

cv2.waitKey(0)