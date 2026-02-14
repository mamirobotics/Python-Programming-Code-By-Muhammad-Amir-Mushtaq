#Lab task 1
#translation
import cv2 #  I use him for image processing
import numpy as np  # for matrix, numerical computation

def translate(image, x, y):#Function to Translate an Image
    M = np.float32([[1, 0, x], [0, 1, y]])
    #Create the Translation Matrix
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    #Apply the Translation
    return shifted

# Load the image
image = cv2.imread(r'C:\Users\Acer\Desktop\SB School\download.jpeg')

# Display the original image
cv2.imshow("Original", image)

# Translate 50 pixels to the right and 30 pixels down
translated = translate(image, 50, 30)
cv2.imshow("Translated", translated)

# Wait for a key press

cv2.waitKey(0)
# and close windows
cv2.destroyAllWindows()
