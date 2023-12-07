from PIL import Image
import numpy as np

# Sobel Kernels
sobel_kernel_x = np.array([
    [-1, 0, 1], 
    [-2, 0, 2], 
    [-1, 0, 1]
    ])

sobel_kernel_y = np.array([
    [-1, -2, -1], 
    [0, 0, 0], 
    [1, 2, 1]
    ])

def convolve_image(image_path, kernel):

    original_image = Image.open(image_path)
    
    image = original_image.convert('L')

    image_data = list(image.getdata())

    width, height = image.size

    image_array = []

    for i in range(height):

        start_index = i*width
        end_index = (i+1) * width

        row_values = image_data[start_index:end_index]
        
        image_array.append(row_values)

    image_array = np.array(image_array, dtype=float)

    image_height, image_width = image_array.shape

    kernel_height, kernel_width = kernel.shape

    convolved_image = np.zeros_like(image_array, dtype=float)

    for i in range(image_height - kernel_height + 1):

        for j in range(image_width - kernel_width + 1):
            
            convolved_image[i, j] = np.sum(image_array[i:i+kernel_height, j:j+kernel_width] * kernel)
    
    return convolved_image

def apply_sobel_filter(image_array):

    gradient_x = convolve_image(image_array, sobel_kernel_x)
    gradient_y = convolve_image(image_array, sobel_kernel_y)

    gradient_magnitude = np.sqrt(np.square(gradient_x) + np.square(gradient_y))

    threshold = 50 
    thresholded_image = Image.fromarray((gradient_magnitude > threshold).astype(np.uint8) * 255)

    return gradient_magnitude, thresholded_image

image_path = 'edge_detection/ytSS.png'
gradient_magnitude, thresholded_image = apply_sobel_filter(image_path)

Image.fromarray(gradient_magnitude.astype(np.uint8)).save('gradient_magnitude_result.png')

output_path = 'edge_detection/output_images/thresholded_result.png'

thresholded_image.save(output_path)








