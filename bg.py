from PIL import Image, ImageEnhance, ImageDraw, ImageChops
import matplotlib.pyplot as plt

# Load the original image
original_image_path = r'C:\\Users\\Acer\\Desktop\\My Document\\Sarfraz Document\\WhatsApp Image 2025-02-23 at 08.10.50_4abd986e.jpg'  # Make sure the path is correct
original_image = Image.open(original_image_path)

# Convert the original image to RGBA (to handle transparency)
original_image = original_image.convert('RGBA')

# Create a mask based on the object's presence
background_color = original_image.getpixel((0, 0))  # Assuming the top-left pixel is the background color
bg = Image.new('RGBA', original_image.size, background_color)
mask = ImageChops.difference(original_image, bg)
mask = ImageChops.add(mask, mask, 2.0, -100)
mask = mask.convert('L')

# Define the colors to apply to each section
colors = [
    (255, 0, 0), (0, 255, 0), (0, 0, 255),
    (255, 255, 0), (255, 0, 255), (0, 255, 255),
    (128, 128, 128), (255, 165, 0), (75, 0, 130)
]

# Create a new blank image with the same size as the original
grid_size = (original_image.width * 3, original_image.height * 3)
new_image = Image.new('RGB', grid_size)

# Place the original image in the center
center_position = (original_image.width, original_image.height)
new_image.paste(original_image.convert('RGB'), center_position)

# Place each image with different background colors around the original image
positions = [
    (0, 0), (original_image.width, 0), (original_image.width * 2, 0),
    (0, original_image.height), center_position, (original_image.width * 2, original_image.height),
    (0, original_image.height * 2), (original_image.width, original_image.height * 2), (original_image.width * 2, original_image.height * 2)
]

for i, position in enumerate(positions):
    if position == center_position:
        continue  # Skip the center position since it's already filled with the original image
    # Create a colored background
    background = Image.new('RGBA', original_image.size, colors[i-1] + (255,))
    # Composite the original image onto the colored background
    combined_image = Image.composite(original_image, background, mask)
    new_image.paste(combined_image.convert('RGB'), position)

# Display the new image
plt.imshow(new_image)
plt.axis('off')  # Hide the axes
plt.show()
