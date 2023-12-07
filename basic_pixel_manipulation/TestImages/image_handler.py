from PIL import Image

def get_image_dimensions(image_path):
    image = Image.open(image_path)
    width, height = image.size
    return width, height

# Returns the unique colours
def find_unique_colors(image_path):

     # Open the image
    image = Image.open(image_path)

    # Get the width and height of the image
    width, height = image.size

    unique_colors = set()

    for x in range(width):
        for y in range(height):

            pixel = image.getpixel((x,y))

            unique_colors.add(pixel)

    return unique_colors

# Crops an image by colour
# TODO: Create new tolerance for each of R G B
def crop_image_by_color(original_img_path, target_color, output_path,tolerance=5):

    original_img = Image.open(original_img_path)

    width, height = original_img.size

    new_img = Image.new("RGBA", (width, height), (0, 0, 0, 0))

    for x in range(width):
        for y in range(height):

            pixel = original_img.getpixel((x,y))

            if all(abs(p - t) <= tolerance for p, t in zip(pixel, target_color)):
                new_img.putpixel((x, y), pixel)

    new_img.save(output_path, format="PNG")
