from PIL import Image, ImageFilter
import cv2
import numpy as np

# Resize the image
def resize_image(input_path, target_width, target_height):

    image = Image.open(input_path)

    resized_image = image.resize((target_width, target_height))

    return resized_image

def apply_blur(input_image, kernel):
    
    image = np.array(input_image)

    blurred_image_array = cv2.filter2D(image, -1, kernel)

    blurred_image = Image.fromarray(blurred_image_array)

    return blurred_image


image_input_path = './test_images/high_vis_test.jpeg'
image_output_path_base = './high_vis_recognition/pre_processed_images/'

target_width = 512
target_height = 512

gaussian_blur_kernel_3x3 = np.array(([1,2,1],
                                 [2,4,2],
                                 [1,2,1])) / 16

gaussian_blur_kernel_5x5 =  np.array([[1, 4, 7, 4, 1],
                                     [4, 16, 26, 16, 4],
                                     [7, 26, 41, 26, 7],
                                     [4, 16, 26, 16, 4],
                                     [1, 4, 7, 4, 1]]) / 273.0

def preprocess_image(image_input_path, target_width, target_height):

    resized_image = resize_image(image_input_path, target_width, target_height)

    resized_image.save(image_output_path_base+'resized_image.jpg')

    blurred_image = apply_blur(resized_image, gaussian_blur_kernel_3x3)

    blurred_image.save(image_output_path_base+'gaussian_blur.jpg')

    return resized_image

preprocess_image(image_input_path, target_width, target_height)