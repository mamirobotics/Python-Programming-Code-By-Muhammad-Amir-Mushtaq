# Lab Task 3
# Flipping
import cv2  #image
import numpy as np  # Matrix deal, Numerical computation

def flip(image, mode): # Make a function
    # mode = 1 → Horizontal flip
    # mode = 0 → Vertical flip
    # mode = -1 → Both horizontal and vertical flip
    flipped = cv2.flip(image, mode)
    return flipped

# Load the image (use the correct path)
image = cv2.imread(r'C:\Users\Acer\Desktop\SB School\download.jpeg')

if image is None:
    print("Error: Image not found. Check the file path.")
else:
    # Perform flipping operations
    flipped_horizontally = flip(image, 1)
    flipped_vertically = flip(image, 0)
    flipped_both = flip(image, -1)

    # Stack all images together
    result = np.hstack((image, flipped_horizontally, flipped_vertically, flipped_both))
    
    # Display the combined image
    cv2.imshow("Original | Horizontal Flip | Vertical Flip | Both Flips", result)
    
    # Wait for a key press and close windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
