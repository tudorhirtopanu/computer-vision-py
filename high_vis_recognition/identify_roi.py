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

def colour_based_segmentation(image_path):
    
    image = cv2.imread(image_path)

    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_color = np.array([25, 100, 100])
    upper_color = np.array([40, 255, 255])

    color_mask = cv2.inRange(hsv_image, lower_color, upper_color)

    segmented_image = cv2.bitwise_and(image, image, mask=color_mask)

    cv2.imshow('Original Image', image)
    cv2.imshow('Color Mask', color_mask)
    cv2.imshow('Segmented Image', segmented_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def identify_roi(preprocessed_image):

    np_image = np.array(preprocessed_image)

    edge_mask = return_edges(np_image)

colour_based_segmentation(image_input_path)