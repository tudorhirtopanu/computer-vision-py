from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def return_frequent_values(image_path, excluded_value):

    image = Image.open(image_path)

    gray_image = image.convert('L')

    gray_image.save('./high_vis_recognition/grayscale_images/grayscale_img.jpg')

    hist = gray_image.histogram()

    plt.plot(hist)

    plt.title('Grayscale Histogram')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    plt.savefig("./high_vis_recognition/histogram") 

    # Find the pixel intensity with the highest frequency (mode), excluding the specified value
    if excluded_value is not None:
        hist[excluded_value] = 0  # Set the frequency of excluded value to 0
    mode_pixel_intensity = np.argmax(hist)

    return mode_pixel_intensity

image_path = './test_images/construction_site_1.jpg'

most_frequent_pixel_intensity = return_frequent_values(image_path, 255)
print(f'Most Frequent Pixel Intensity: {most_frequent_pixel_intensity}')