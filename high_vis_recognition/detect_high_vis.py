from PIL import Image

def resize_image(input_path, output_path, target_width, target_height):

    image = Image.open(input_path)

    resized_image = image.resize((target_width, target_height))

    resized_image.save(output_path)

input_image_path = './test_images/construction_site_1.jpg'
output_image_path = './high_vis_recognition/resized_images/resized_image.jpg'

target_width = 640
target_height = 480

resize_image(input_image_path, output_image_path, target_width, target_height)