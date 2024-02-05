import cv2

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')

image = cv2.imread('test_images/w3.jpeg')

gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Params:
# scaleFactor - specifying how much the image size is reduced at each image scale.
# minNeighbours - specifies how many neighboring rectangles need to agree that a region is a detected object
# minSize - sets the smallest object size you want to detect
# maxSize - sets the largest object size you want to detect

faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=3)
for (x, y, w, h) in faces:
    print(x,y,w,h)
    roi_gray = gray_img[y:y+h, x:x+w]
    roi_color = gray_img[y:y+h, x:x+w]
    img_item = "img.png"
    cv2.imwrite(img_item, roi_gray)
    
    color = (255, 0, 0)
    stroke = 2
    end_cord_x = x + w
    end_cord_y = y + h
    cv2.rectangle(image, (x,y), (end_cord_x, end_cord_y), color, stroke)

cv2.imshow('face detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()