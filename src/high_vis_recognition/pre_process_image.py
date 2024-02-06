import cv2
import numpy as np

image_input_path = './test_images/high_vis_2.jpg'
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

# convert image to a numpy array
def image_path_to_numpy_array(image_path):

    image_array = cv2.imread(image_path)

    return image_array

# Resize the image
def resize_image(image_array, target_width, target_height):

    resized_image = cv2.resize(image_array, (target_width, target_height))

    return resized_image

def apply_blur(image_array, kernel):

    blurred_image_array = cv2.filter2D(image_array, -1, kernel)

    #convert array to image
    #blurred_image = Image.fromarray(blurred_image_array)

    return blurred_image_array

def preprocess_image(image_input_path, target_width, target_height):

    #image_array = image_path_to_numpy_array(image_input_path)

    #resized_image = resize_image(image_array, target_width, target_height)

    resized_image = resize_image(image_input_path, target_width, target_height)

    blurred_image = apply_blur(resized_image, gaussian_blur_kernel_5x5)

    return blurred_image

#preprocess_image(image_input_path, target_width, target_height)