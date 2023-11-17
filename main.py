from PIL import Image

# Open a JPG image file
image = Image.open("testImage.jpg")

# Define the coordinates (x, y) of the pixel you want to check
x = 100
y = 50

# Get the RGB values of a pixel at coordinates (x, y)
pixel_color = image.getpixel((x, y))

print("Pixel color:", pixel_color)
print("RGB values of pixel at ({}, {}): {}".format(x, y, pixel_color))