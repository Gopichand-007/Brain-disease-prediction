import cv2
import numpy as np
import os

def preprocess_image(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (224, 224))
    img = img / 255.0
    return img

if __name__ == "__main__":
    sample_image = "data/sample_mri.jpg"
    if os.path.exists(sample_image):
        processed = preprocess_image(sample_image)
        print("Preprocessed Image Shape:", processed.shape)
