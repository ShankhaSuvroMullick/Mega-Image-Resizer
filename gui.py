# gui.py
from tkinter import Tk, filedialog, simpledialog
from PIL import Image
import cv2
from tts import speak

def gui_file_picker_resize():
    """
    GUI dialog to select an image and resize via Pillow + Tkinter.
    """
    Tk().withdraw()
    file_path = filedialog.askopenfilename(title="Select image")
    if not file_path:
        return
    img = Image.open(file_path)
    w = simpledialog.askinteger("Width", "Enter new width")
    h = simpledialog.askinteger("Height", "Enter new height")
    resized = img.resize((w, h), Image.LANCZOS)
    resized.save("resized_gui.jpg")
    speak(f"Image resized to width {w} and height {h}")
    print("✅ Saved resized_gui.jpg")
    return resized

def gui_opencv_slider():
    """
    GUI slider to dynamically resize image width/height using OpenCV.
    """
    from tkinter import filedialog
    file_path = filedialog.askopenfilename(title="Select image")
    if not file_path:
        return
    img = cv2.imread(file_path)
    cv2.namedWindow("Resize Slider")
    cv2.createTrackbar("Width", "Resize Slider", img.shape[1], img.shape[1]*2, lambda x: None)
    cv2.createTrackbar("Height", "Resize Slider", img.shape[0], img.shape[0]*2, lambda x: None)
    while True:
        w = cv2.getTrackbarPos("Width", "Resize Slider")
        h = cv2.getTrackbarPos("Height", "Resize Slider")
        resized = cv2.resize(img, (max(w,1), max(h,1)))
        cv2.imshow("Resize Slider", resized)
        if cv2.waitKey(1) & 0xFF == 27:
            cv2.imwrite("resized_slider.jpg", resized)
            speak(f"Image resized to width {w} and height {h}")
            break
    cv2.destroyAllWindows()
    print("✅ Saved resized_slider.jpg")
    return resized
