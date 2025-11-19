"""
Mega Image Resizer
Author: Your Name
Date: 2025-11-19

Description:
A Python program that allows resizing images in multiple ways:
1) Fixed width/height using OpenCV
2) Fixed width/height using Pillow
3) Resize by percentage
4) Batch resize images in a folder
5) GUI resize using Pillow + Tkinter
6) GUI resize using OpenCV sliders

Additional Features:
- Text-to-Speech notifications using pyttsx3
- Side-by-side display of original and resized images using matplotlib
"""

# --- IMPORT MODULES ---
import os  # Operating system module for folder/file management
import cv2  # OpenCV for image processing and GUI sliders
from PIL import Image  # Pillow for image processing
import pyttsx3  # Text-to-Speech
from tkinter import Tk, filedialog, simpledialog  # GUI dialogs
import matplotlib.pyplot as plt  # For displaying images

# --- INITIALIZE TEXT-TO-SPEECH ENGINE ---
engine = pyttsx3.init()

def speak(text: str) -> None:
    """
    Converts text to speech.

    Parameters:
    text (str): The text to speak.

    Returns:
    None
    """
    engine.say(text)
    engine.runAndWait()


# --- 1) FIXED RESIZE USING OPENCV ---
def resize_fixed_cv(image_path: str, width: int, height: int, output_name: str = "resized_cv.jpg"):
    """
    Resize image to a fixed width and height using OpenCV.

    Parameters:
    image_path (str): Path to the input image.
    width (int): Desired width.
    height (int): Desired height.
    output_name (str): Filename for the saved resized image.

    Returns:
    numpy.ndarray: The resized image as an array.
    """
    img = cv2.imread(image_path)  # Read image as a NumPy array
    if img is None:  # Check if image exists
        print("❌ ERROR: Image not found")
        return
    resized = cv2.resize(img, (width, height))  # Resize to specified dimensions
    cv2.imwrite(output_name, resized)  # Save resized image
    speak(f"Image resized to width {width} and height {height}")  # Notify user
    return resized


# --- 2) FIXED RESIZE USING PILLOW ---
def resize_fixed_pil(image_path: str, width: int, height: int, output_name: str = "resized_pil.jpg"):
    """
    Resize image to a fixed width and height using Pillow.

    Parameters:
    image_path (str): Path to the input image.
    width (int): Desired width.
    height (int): Desired height.
    output_name (str): Filename for the saved resized image.

    Returns:
    PIL.Image.Image: The resized image object.
    """
    img = Image.open(image_path)
    resized = img.resize((width, height), RESAMPLE_FILTER)  # Smooth resizing
    resized.save(output_name)
    speak(f"Image resized to width {width} and height {height}")
    return resized


# --- 3) RESIZE BY PERCENTAGE ---
def resize_percentage(image_path: str, percent: int, output_name: str = "resized_percent.jpg"):
    """
    Resize image by a percentage of original size.

    Parameters:
    image_path (str): Path to the input image.
    percent (int): Resize percentage (e.g., 50 = reduce to 50%).
    output_name (str): Filename for saved resized image.

    Returns:
    PIL.Image.Image: The resized image object.
    """
    img = Image.open(image_path)
    w, h = img.size  # Get original dimensions
    resized = img.resize((int(w * percent / 100), int(h * percent / 100)), Image.ANTIALIAS)
    resized.save(output_name)
    speak(f"Image resized to {percent}% of original size")
    return resized


# --- 4) BATCH RESIZE FOLDER ---
def batch_resize(folder: str, width: int, height: int, output_folder: str = "resized_batch"):
    """
    Resize all images in a folder to fixed width and height.

    Parameters:
    folder (str): Path to folder containing images.
    width (int): Desired width for all images.
    height (int): Desired height for all images.
    output_folder (str): Folder to save resized images.

    Returns:
    None
    """
    os.makedirs(output_folder, exist_ok=True)  # Create folder if it doesn't exist
    for f in os.listdir(folder):
        if f.lower().endswith((".png", ".jpg", ".jpeg")):
            img = Image.open(os.path.join(folder, f))
            img.resize((width, height)).save(os.path.join(output_folder, f"resized_{f}"))
    speak(f"Batch resize complete for folder {folder}")


# --- 5) DISPLAY ORIGINAL AND RESIZED SIDE-BY-SIDE ---
def display_with_matplotlib(original, resized):
    """
    Display original and resized images side-by-side using matplotlib.

    Parameters:
    original (numpy.ndarray or PIL.Image.Image): Original image.
    resized (numpy.ndarray or PIL.Image.Image): Resized image.

    Returns:
    None
    """
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    # Convert OpenCV images from BGR to RGB if needed
    if isinstance(original, type(cv2.imread(''))):
        axs[0].imshow(cv2.cvtColor(original, cv2.COLOR_BGR2RGB))
    else:
        axs[0].imshow(original)
    axs[0].axis('off')
    axs[0].set_title("Original")

    if isinstance(resized, type(cv2.imread(''))):
        axs[1].imshow(cv2.cvtColor(resized, cv2.COLOR_BGR2RGB))
    else:
        axs[1].imshow(resized)
    axs[1].axis('off')
    axs[1].set_title("Resized")
    plt.show()


# --- 6) GUI FILE PICKER RESIZE (Tkinter + PIL) ---
def gui_file_picker_resize():
    """
    GUI dialog to select an image and resize it via user input width/height.

    Returns:
    PIL.Image.Image: Resized image.
    """
    Tk().withdraw()  # Hide root Tk window
    file_path = filedialog.askopenfilename(title="Select image")
    if not file_path:
        return
    img = Image.open(file_path)
    w = simpledialog.askinteger("Width", "Enter new width")
    h = simpledialog.askinteger("Height", "Enter new height")
    resized = img.resize((w, h), Image.ANTIALIAS)
    resized.save("resized_gui.jpg")
    speak(f"Image resized to width {w} and height {h}")
    print("✅ Saved resized_gui.jpg")
    return resized


# --- 7) GUI OPENCV SLIDER RESIZE ---
def gui_opencv_slider():
    """
    GUI slider to dynamically resize image width/height using OpenCV trackbars.

    Returns:
    numpy.ndarray: Resized image.
    """
    file_path = filedialog.askopenfilename(title="Select image")
    if not file_path:
        return
    img = cv2.imread(file_path)
    cv2.namedWindow("Resize Slider")
    # Create sliders
    cv2.createTrackbar("Width", "Resize Slider", img.shape[1], img.shape[1]*2, lambda x: None)
    cv2.createTrackbar("Height", "Resize Slider", img.shape[0], img.shape[0]*2, lambda x: None)
    while True:
        w = cv2.getTrackbarPos("Width", "Resize Slider")
        h = cv2.getTrackbarPos("Height", "Resize Slider")
        resized = cv2.resize(img, (max(w,1), max(h,1)))
        cv2.imshow("Resize Slider", resized)
        if cv2.waitKey(1) & 0xFF == 27:  # ESC key to exit
            cv2.imwrite("resized_slider.jpg", resized)
            speak(f"Image resized to width {w} and height {h}")
            break
    cv2.destroyAllWindows()
    print("✅ Saved resized_slider.jpg")
    return resized


# --- 8) MAIN MENU LOOP ---
def main_menu():
    """
    Main menu interface for Mega Image Resizer.
    Allows user to choose resizing method.
    """
    while True:
        print("\n=== Mega Image Resizer ===")
        print("1) Resize fixed (OpenCV CLI)")
        print("2) Resize fixed (Pillow CLI)")
        print("3) Resize by percentage")
        print("4) Batch resize folder")
        print("5) GUI resize (PIL + Tkinter)")
        print("6) GUI resize (OpenCV slider)")
        print("0) Exit")
        choice = input("Choice: ")
        if choice == "1":
            path = input("Path: ")
            w = int(input("Width: "))
            h = int(input("Height: "))
            img_resized = resize_fixed_cv(path, w, h)
            display_with_matplotlib(cv2.imread(path), img_resized)
        elif choice == "2":
            path = input("Path: ")
            w = int(input("Width: "))
            h = int(input("Height: "))
            resize_fixed_pil(path, w, h)
        elif choice == "3":
            path = input("Path: ")
            pct = int(input("Percent: "))
            resize_percentage(path, pct)
        elif choice == "4":
            folder = input("Folder: ")
            w = int(input("Width: "))
            h = int(input("Height: "))
            batch_resize(folder, w, h)
        elif choice == "5":
            gui_file_picker_resize()
        elif choice == "6":
            gui_opencv_slider()
        elif choice == "0":
            print("Exiting Mega Image Resizer...")
            break
        else:
            print("❌ Invalid choice")


# --- RUN PROGRAM ---
if __name__ == "__main__":
    main_menu()
