from high_vis_recognition.pre_process_image import preprocess_image
from high_vis_recognition.identify_roi import identify_roi
import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')

image = cv2.imread('test_images/peoplehv_3.jpg')

gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Params:
# scaleFactor - specifying how much the image size is reduced at each image scale.
# minNeighbours - specifies how many neighboring rectangles need to agree that a region is a detected object
# minSize - sets the smallest object size you want to detect
# maxSize - sets the largest object size you want to detect

faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=3)

if len(faces) == 0:
        print("No Person Detected")

for (x, y, w, h) in faces:

    print(x,y,w,h)
    
    ### Rectangle for Detected Faces ###
    color = (255, 0, 0)
    stroke = 2
    end_cord_x = x + w
    end_cord_y = y + h

    # draw the rectangle
    cv2.rectangle(image, (x,y), (end_cord_x, end_cord_y), color, stroke)

    ### Torso Rectangle ###
    second_rectangle_y = y + h  

    second_start_cord_x = int(x - (h ))
    second_end_cord_x = int(x + (2*h ))

    second_end_cord_y = end_cord_y + h* 4
    
    # Draw the second rectangle
    cv2.rectangle(image, (second_start_cord_x, second_rectangle_y), (second_end_cord_x, second_end_cord_y), color, stroke)

    # Currently the code is only effective on one person

    ### Look for High Vis on Torso ###
    roi_torso = image[second_rectangle_y:second_end_cord_y, second_start_cord_x:second_end_cord_x]
    roi_torso_array = np.array(roi_torso)
    # pre process image
    pre_processed_image = preprocess_image(roi_torso_array, 500, 500)

    # identify roi
    filtered_image, segmented_image = identify_roi(pre_processed_image)
    cv2.imwrite("filteredImg.jpg", filtered_image)

    is_empty = np.all(filtered_image == 0)

    if is_empty:
        print("The person is NOT wearing a high vis.")
    else:
        print("The person is wearing a high vis")

cv2.imshow('face detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()