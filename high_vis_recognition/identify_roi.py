import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

image_input_path = './high_vis_recognition/pre_processed_images/gaussian_blur.jpg'
image_output_path_base = './high_vis_recognition/roi_images/'

lower_color_green = np.array([30, 100, 100])
upper_color_green = np.array([40, 255, 255])

# image to be a numpy array
def return_edges(image):

    edges = cv2.Canny(image, 90, 150)
    #edges_image = Image.fromarray(edges)
    #edges_image.save(image_output_path_base + 'edges.jpg')
    return edges

def colour_based_segmentation(image_array):

    hsv_image = cv2.cvtColor(image_array, cv2.COLOR_BGR2HSV)

    #lower_color_orange = np.array([10, 100, 100])
    #upper_color_orange = np.array([20, 255, 255])   

    #mask_green = cv2.inRange(hsv_image, lower_color_green, upper_color_green) 
    #mask_orange = cv2.inRange(hsv_image, lower_color_green, upper_color_green) 

    #final_mask = cv2.bitwise_or(mask_green, mask_orange)

    color_mask = cv2.inRange(hsv_image, lower_color_green, upper_color_green)

    segmented_image = cv2.bitwise_and(image_array, image_array, mask=color_mask)

    return segmented_image

def get_contours(segmented_image, min_contour_area=150):
    # Find contours in the binary image
    contours, _ = cv2.findContours(cv2.cvtColor(segmented_image, cv2.COLOR_BGR2GRAY), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filter contours based on area
    filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_contour_area]

    # Create an empty mask
    mask = np.zeros_like(segmented_image)

    # Draw contours on the mask
    cv2.drawContours(mask, filtered_contours, -1, (255, 255, 255), thickness=cv2.FILLED)

    # Apply the mask to the original image
    result_image = cv2.bitwise_and(segmented_image, mask)

    return result_image

def identify_roi(preprocessed_image_array):
    edges = return_edges(preprocessed_image_array)
    segmented_image = colour_based_segmentation(preprocessed_image_array)

    # Filter edges based on the presence of segmented color
    edges_with_color = cv2.bitwise_and(edges, edges, mask=cv2.cvtColor(segmented_image, cv2.COLOR_BGR2GRAY))

    combined_image = cv2.addWeighted(segmented_image, 1, cv2.cvtColor(edges_with_color, cv2.COLOR_GRAY2BGR), 1, 0)

    filer_by_contour = get_contours(combined_image)

    return filer_by_contour, combined_image

    

#colour_based_segmentation(image_input_path)

#cv2.imshow('Original Image', image)
#cv2.imshow('Color Mask', color_mask)
#cv2.imshow('Segmented Image', segmented_image)
#cv2.waitKey(0)
#cv2.destroyAllWindows()