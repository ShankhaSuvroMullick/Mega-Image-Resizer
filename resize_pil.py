# resize_pil.py
from PIL import Image
from tts import speak

RESAMPLE_FILTER = Image.LANCZOS  # Smooth resizing

def resize_fixed_pil(image_path: str, width: int, height: int, output_name: str = "resized_pil.jpg"):
    """
    Resize image to a fixed width and height using Pillow.
    """
    img = Image.open(image_path)
    resized = img.resize((width, height), RESAMPLE_FILTER)
    resized.save(output_name)
    speak(f"Image resized to width {width} and height {height}")
    return resized

def resize_percentage(image_path: str, percent: int, output_name: str = "resized_percent.jpg"):
    """
    Resize image by a percentage of original size.
    """
    img = Image.open(image_path)
    w, h = img.size
    resized = img.resize((int(w * percent / 100), int(h * percent / 100)), RESAMPLE_FILTER)
    resized.save(output_name)
    speak(f"Image resized to {percent}% of original size")
    return resized

def batch_resize(folder: str, width: int, height: int, output_folder: str = "resized_batch"):
    """
    Resize all images in a folder to fixed width and height.
    """
    import os
    os.makedirs(output_folder, exist_ok=True)
    for f in os.listdir(folder):
        if f.lower().endswith((".png", ".jpg", ".jpeg")):
            img = Image.open(os.path.join(folder, f))
            img.resize((width, height)).save(os.path.join(output_folder, f"resized_{f}"))
    speak(f"Batch resize complete for folder {folder}")
