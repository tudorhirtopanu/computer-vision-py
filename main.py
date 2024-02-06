import cv2
import numpy as np
from high_vis_recognition.pre_process_image import preprocess_image
from high_vis_recognition.identify_roi import identify_roi, return_edges

input_image_path = "test_images/high_vis_test.jpeg"
target_width = 300
target_height = 300

original_image = cv2.imread(input_image_path)

preprocessed_image = preprocess_image(input_image_path, target_width, target_height)

edges_image = return_edges(preprocessed_image)

filtered_image, segmented_image = identify_roi(preprocessed_image)

cv2.imshow("original image", original_image)
cv2.imshow("edges", edges_image)
cv2.imshow("image", segmented_image)
cv2.imshow("filtered image", filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()