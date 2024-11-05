import numpy as np
import cv2
from PIL import Image

def preprocess_image(img):
    # Convert to grey image if colored
    grey_img = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY)
    
    # Resize image 
    resized_img = cv2.resize(grey_img, None, fx= 1.5, fy= 1.5, interpolation=cv2.INTER_LINEAR)
    
    # Process image by adding adaptive threshold
    processed_image = cv2.adaptiveThreshold(
    resized_img, 255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv2.THRESH_BINARY,
    61,
    11)
    return processed_image