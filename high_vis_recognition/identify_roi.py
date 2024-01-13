import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

image_input_path = './high_vis_recognition/pre_processed_images/gaussian_blur.jpg'
image_output_path_base = './high_vis_recognition/roi_images/'

# image to be a numpy array
def return_edges(image):

    edges = cv2.Canny(image, 50, 150)
    edges_image = Image.fromarray(edges)
    edges_image.save(image_output_path_base + 'edges.jpg')
    return edges

def colour_based_segmentation(image_array):

    hsv_image = cv2.cvtColor(image_array, cv2.COLOR_BGR2HSV)

    lower_color_green = np.array([30, 100, 100])
    upper_color_green = np.array([40, 255, 255])

    lower_color_orange = np.array([10, 100, 100])
    upper_color_orange = np.array([20, 255, 255])   

    mask_green = cv2.inRange(hsv_image, lower_color_green, upper_color_green) 
    mask_orange = cv2.inRange(hsv_image, lower_color_orange, upper_color_orange) 

    final_mask = cv2.bitwise_or(mask_green, mask_orange)

    #color_mask = cv2.inRange(hsv_image, lower_color, upper_color)

    segmented_image = cv2.bitwise_and(image_array, image_array, mask=final_mask)

    return segmented_image

def identify_roi(preprocessed_image_array):

    image_array = colour_based_segmentation(preprocessed_image_array)

    return image_array

    

#colour_based_segmentation(image_input_path)

#cv2.imshow('Original Image', image)
#cv2.imshow('Color Mask', color_mask)
#cv2.imshow('Segmented Image', segmented_image)
#cv2.waitKey(0)
#cv2.destroyAllWindows()