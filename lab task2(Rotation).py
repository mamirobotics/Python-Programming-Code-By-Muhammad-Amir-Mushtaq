# Lab Task 2
# Rotation
import cv2
import numpy as np
#Function to Rotate an Image
def rotate(image, angle):
    # Get Image Dimensions
    (h, w) = image.shape[:2]
    #Calculate the Center of the Image
    center = (w // 2, h // 2)
    # Get the rotation matrix
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    #Apply the Rotation
    rotated = cv2.warpAffine(image, M, (w, h))
    return rotated

# Load the image (use the correct path)
image = cv2.imread(r'C:\Users\Acer\Desktop\SB School\download.jpeg')

if image is None:
    print("Error: Image not found. Check the file path.")
else:
    # Rotate images at different angles
    rotated_0 = rotate(image, 0)
    rotated_90 = rotate(image, 90)
    rotated_180 = rotate(image, 180)
    rotated_270 = rotate(image, 270)
    
    # Stack all rotated images horizontally
    result = np.hstack((rotated_0, rotated_90, rotated_180, rotated_270))
    
    # Display the combined image
    cv2.imshow("Rotated Images (0°, 90°, 180°, 270°)", result)
    
    # Wait for a key press and close windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
