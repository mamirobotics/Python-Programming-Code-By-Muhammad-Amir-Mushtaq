import numpy as np
import cv2
import argparse 
import imutils

# Directly read the image file
image = cv2.imread(r"C:\Users\Acer\Desktop\SB School\download.jpeg")
cv2.imshow("Original", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Shift down and right
M = np.float32([[1, 0, 25], [0, 1, 50]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Down and Right", shifted)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Shift up and left
M = np.float32([[1, 0, -50], [0, 1, -90]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Up and Left", shifted)
cv2.waitKey(0)
cv2.destroyAllWindows()


def translate(image, x, y):
    M = np.float32([[1, 0, x], [0, 1, y]])
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    return shifted
shifted = translate(image, 0, 100)
cv2.imshow("Shifted Down", shifted)
cv2.waitKey(0)
