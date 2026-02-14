#Lab No 5
#Lab task 4
#Cropping
#import library
'''import cv2
#Define the Cropping Function
def crop(image, y1, y2, x1, x2):
     #Get Image Dimensions
    height, width = image.shape[:2]
    # Ensure Cropping Coordinates Are Within Bounds
    y1, y2 = max(0, y1), min(height, y2)
    x1, x2 = max(0, x1), min(width, x2)
    #Here we Crop the Image
    cropped = image[y1:y2, x1:x2]
    return cropped

# Load the image
image = cv2.imread(r'C:\Users\Acer\Desktop\Semester 6 Data\Digital image lab data\Brachiosaurus_BW.jpg')

if image is None:
    print("Error: Image not found. Check the file path.")
else:
    cropped = crop(image, 50, 150, 690, 780)#Crop the Image Using the Defined Function

    if cropped.size == 0:
        print("Error: Cropping failed. Check the coordinates.")
    else:
        # Resize to medium size
        cropped_resized = cv2.resize(cropped, (200, 200))

        cv2.imshow("Original", image)
        cv2.imshow("Cropped", cropped_resized)
        
        cv2.waitKey(0)
        cv2.destroyAllWindows()
'''
#Lab No 5
#Lab task 4
#Cropping
import cv2
import os # Import the os module for path manipulation

# --- Define the Cropping Function ---
def crop(image, y1, y2, x1, x2):
    # Get Image Dimensions
    height, width = image.shape[:2]
    
    # Ensure Cropping Coordinates Are Within Bounds
    # This prevents indexing errors and ensures the crop area is valid.
    y1, y2 = max(0, y1), min(height, y2)
    x1, x2 = max(0, x1), min(width, x2)
    
    # Ensure valid coordinate order (y1 < y2 and x1 < x2)
    y1, y2 = min(y1, y2), max(y1, y2)
    x1, x2 = min(x1, x2), max(x1, x2)
    
    # Here we Crop the Image
    cropped = image[y1:y2, x1:x2]
    return cropped

# --- Image Loading ---


image = cv2.imread('C:\Users\Acer\Desktop\Semester 6 Data\Digital image lab data\Brachiosaurus_BW.jpg')
# Load the image
image = cv2.imread(file_path)

# --- Error Handling and Execution ---
if image is None:
    # Most common error: Image not found. Provide helpful context.
    print(f"Error: Image not found at path: \n{file_path}")
    print("\nPlease ensure the file path is correct or try placing the image in the same folder as the Python script and using its name.")
else:
    # 💡 The coordinates for cropping are (50, 150) for Y and (690, 780) for X.
    cropped = crop(image, 50, 150, 690, 780)

    if cropped.size == 0:
        # This means the cropping area was outside the image dimensions.
        print("Error: Cropping failed. The specified coordinates resulted in an empty image.")
        print(f"Image Dimensions: Height={image.shape[0]}, Width={image.shape[1]}")
    else:
        # Resize the cropped image for better viewing
        cropped_resized = cv2.resize(cropped, (200, 200))

        # Show the images
        cv2.imshow("Original Image", image)
        cv2.imshow("Cropped and Resized", cropped_resized)
        
        # Wait indefinitely for a key press and then close all windows
        cv2.waitKey(0)
        cv2.destroyAllWindows()