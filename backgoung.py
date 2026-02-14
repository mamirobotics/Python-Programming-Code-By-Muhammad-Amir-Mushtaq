from PIL import Image, ImageEnhance, ImageDraw
import matplotlib.pyplot as plt

# Load the original image
original_image_path = r'C:\\Users\\Acer\\Desktop\\My Document\\Sarfraz Document\\WhatsApp Image 2025-02-23 at 08.10.50_4abd986e.jpg'  # Make sure the path is correct
original_image = Image.open(original_image_path)

# Define the colors to apply to each section
colors = [
    (255, 0, 0), (0, 255, 0), (0, 0, 255),
    (255, 255, 0), (255, 0, 255), (0, 255, 255),
    (128, 128, 128), (255, 165, 0), (75, 0, 130)
]

# Create a new blank image with the same size as the original
new_image = Image.new('RGB', (original_image.width * 3, original_image.height * 3))

# Define the shades to apply to each copy
shades = [0.3, 0.5, 0.7, 0.9, 1.0, 1.1, 1.3, 1.5, 1.7]

# Place each shaded image in the grid with different background colors
for i in range(3):
    for j in range(3):
        index = i * 3 + j
        # Create a colored background
        background = Image.new('RGB', (original_image.width, original_image.height), colors[index])
        enhancer = ImageEnhance.Brightness(original_image)
        shaded_image = enhancer.enhance(shades[index])
        # Combine the shaded image with the colored background
        combined_image = Image.blend(background, shaded_image, alpha=0.5)
        new_image.paste(combined_image, (j * original_image.width, i * original_image.height))

# Display the new image
plt.imshow(new_image)
plt.axis('off')  # Hide the axes
plt.show()
