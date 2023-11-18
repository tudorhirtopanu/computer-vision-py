from PIL import Image
from image_handler import get_image_dimensions, find_unique_colors, crop_image_by_color

path_to_image = "TestImages/ps1.png"

target_color = (207, 50, 201)

output_path = "CroppedImages/cropped_image.jpg"

# Get a unique color from the original image
unique_color = find_unique_colors(path_to_image)

print(unique_color) 

crop_image_by_color(path_to_image, target_color,output_path)

# TODO: Iterate over all pixels and keep track of ones with selected colour then return new image
