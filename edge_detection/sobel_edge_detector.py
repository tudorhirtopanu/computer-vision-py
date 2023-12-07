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

# Convert image to grayscale
def convert_to_grayscale(image, output_path=None):
    original_image = Image.open(image)

    grayscale_image = original_image.convert('L')

    if output_path:
        grayscale_image.save(output_path)

    return grayscale_image

def convolve_image(image_path, kernel):

    original_image = Image.open(image_path)
    
    image = original_image.convert('L')

    image_data = list(image.getdata())

    width, height = image.size

    # TODO: handle case where image dimensions arent multiples of kernel size 
    image_array = []

    for i in range(height):

        start_index = i*width
        end_index = (i+1) * width

        # Slice the flattened image_data to get the current row
        row_values = image_data[start_index:end_index]

        image_array.append(row_values)

    image_array = np.array(image_array, dtype=float)

    # Apply zero-padding to the image_array
    padded_image = np.pad(image_array, ((1, 1), (1, 1)), mode='constant')

    result = np.zeros_like(image_array, dtype=float)

    for i in range(height - kernel.shape[0]+1):
        for j in range(width - kernel.shape[1] + 1):
            result[i, j] = np.sum(image_array[i:i+kernel.shape[0], j:j+kernel.shape[1]] * kernel)
    
    return result

def apply_sobel_filter(image_array):

    gradient_x = convolve_image(image_array, sobel_kernel_x)
    gradient_y = convolve_image(image_array, sobel_kernel_y)

    gradient_magnitude = np.sqrt(np.square(gradient_x) + np.square(gradient_y))

    # Apply thresholding
    threshold = 50  # Adjust the threshold as needed
    thresholded_image = Image.fromarray((gradient_magnitude > threshold).astype(np.uint8) * 255)

    return gradient_magnitude, thresholded_image

test_image_path = 'edge_detection/lionps.png'

image_path = 'edge_detection/lionps.png'
gradient_magnitude, thresholded_image = apply_sobel_filter(image_path)

# Save the gradient magnitude result as an image
Image.fromarray(gradient_magnitude.astype(np.uint8)).save('gradient_magnitude_result.png')

# Save the thresholded image
thresholded_image.save('thresholded_result.png')








