# resize_cv.py
import cv2
from tts import speak

def resize_fixed_cv(image_path: str, width: int, height: int, output_name: str = "resized_cv.jpg"):
    """
    Resize image to a fixed width and height using OpenCV.

    Returns the resized image as a NumPy array.
    """
    img = cv2.imread(image_path)
    if img is None:
        print("❌ ERROR: Image not found")
        return
    resized = cv2.resize(img, (width, height))
    cv2.imwrite(output_name, resized)
    speak(f"Image resized to width {width} and height {height}")
    return resized
