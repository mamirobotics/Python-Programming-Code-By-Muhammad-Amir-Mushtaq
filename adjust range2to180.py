from PIL import Image, ImageEnhance
import matplotlib.pyplot as plt

# Load the original image
original_image_path = r'C:\\Users\\Acer\\Desktop\\My Document\\Sarfraz Document\\WhatsApp Image 2025-02-23 at 08.10.50_4abd986e.jpg'  # Make sure the path is correct
original_image = Image.open(original_image_path)

# Create a new blank image with the same size as the original
new_image = Image.new('RGB', (original_image.width * 10, original_image.height * 10))

# Define the shades to apply to each copy
shades = [2 + (i * 178 / 99) for i in range(100)]  # Generate 100 different shades in the range of 2-180

# Place each shaded image in the grid
for i in range(10):
    for j in range(10):
        index = i * 10 + j
        enhancer = ImageEnhance.Brightness(original_image)
        shaded_image = enhancer.enhance(shades[index] / 100)
        new_image.paste(shaded_image, (j * original_image.width, i * original_image.height))

# Display the new image
plt.imshow(new_image)
plt.axis('off')  # Hide the axes
plt.show()
