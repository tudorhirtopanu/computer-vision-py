import cv2
import numpy as np
from high_vis_recognition.pre_process_image import preprocess_image
from high_vis_recognition.identify_roi import identify_roi, colour_based_segmentation

input_image_path = "test_images/construction_site_1.jpg"
target_width = 512
target_height = 512

original_image = cv2.imread(input_image_path)

preprocessed_image = preprocess_image(input_image_path, target_width, target_height)

segmented_image = identify_roi(preprocessed_image)

cv2.imshow("original image", original_image)
cv2.imshow("image", segmented_image)
cv2.waitKey(0)
cv2.destroyAllWindows()