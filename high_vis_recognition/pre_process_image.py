from PIL import Image, ImageFilter
import numpy as np

# Resize the image
def resize_image(input_path, target_width, target_height):

    image = Image.open(input_path)

    resized_image = image.resize((target_width, target_height))

    return resized_image

image_input_path = './test_images/parking_warden_3.jpg'
image_output_path = './high_vis_recognition/pre_processed_images/pre_processed_image.jpg'
image_output_path_base = './high_vis_recognition/pre_processed_images/'

target_width = 512
target_height = 512

def preprocess_image(image_input_path, target_width, target_height):

    resized_image = resize_image(image_input_path, target_width, target_height)

    resized_image.save(image_output_path_base+'resized_image.jpg')

    noise_reduced_image = resized_image.filter(ImageFilter.GaussianBlur(1))

    noise_reduced_image.save(image_output_path_base+'noise_reduced_image.jpg')

    return resized_image

preprocess_image(image_input_path, target_width, target_height)