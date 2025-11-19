# Program 8: Mega Image Resizer
import os
import cv2
from PIL import Image
import pyttsx3
from tkinter import Tk, filedialog, simpledialog
import matplotlib.pyplot as plt

engine = pyttsx3.init()
def speak(text): engine.say(text); engine.runAndWait()

def resize_fixed_cv(image_path, width, height, output_name="resized_cv.jpg"):
    img = cv2.imread(image_path)
    if img is None: return
    resized = cv2.resize(img, (width, height))
    cv2.imwrite(output_name, resized)
    speak(f"Image resized to width {width} and height {height}")
    return resized

def resize_fixed_pil(image_path, width, height, output_name="resized_pil.jpg"):
    img = Image.open(image_path)
    resized = img.resize((width, height), Image.ANTIALIAS)
    resized.save(output_name)
    speak(f"Image resized to width {width} and height {height}")
    return resized

def resize_percentage(image_path, percent, output_name="resized_percent.jpg"):
    img = Image.open(image_path)
    w, h = img.size
    resized = img.resize((int(w*percent/100), int(h*percent/100)), Image.ANTIALIAS)
    resized.save(output_name)
    speak(f"Image resized to {percent}%")
    return resized

def batch_resize(folder, width, height, output_folder="resized_batch"):
    os.makedirs(output_folder, exist_ok=True)
    for f in os.listdir(folder):
        if f.lower().endswith((".png",".jpg",".jpeg")):
            img = Image.open(os.path.join(folder, f))
            img.resize((width,height)).save(os.path.join(output_folder,f"resized_{f}"))
    speak(f"Batch resize complete for folder {folder}")

def display_with_matplotlib(original,resized):
    fig, axs = plt.subplots(1,2, figsize=(10,5))
    axs[0].imshow(cv2.cvtColor(original, cv2.COLOR_BGR2RGB) if isinstance(original,type(cv2.imread(''))) else original)
    axs[0].axis('off'); axs[0].set_title("Original")
    axs[1].imshow(cv2.cvtColor(resized, cv2.COLOR_BGR2RGB) if isinstance(resized,type(cv2.imread(''))) else resized)
    axs[1].axis('off'); axs[1].set_title("Resized")
    plt.show()

def gui_file_picker_resize():
    Tk().withdraw()
    file_path = filedialog.askopenfilename(title="Select image")
    if not file_path: return
    img = Image.open(file_path)
    w = simpledialog.askinteger("Width","Enter new width")
    h = simpledialog.askinteger("Height","Enter new height")
    resized = img.resize((w,h), Image.ANTIALIAS)
    resized.save("resized_gui.jpg")
    speak(f"Image resized to width {w} and height {h}")
    print("✅ Saved resized_gui.jpg")
    return resized

def gui_opencv_slider():
    file_path = filedialog.askopenfilename(title="Select image")
    if not file_path: return
    img = cv2.imread(file_path)
    cv2.namedWindow("Resize Slider")
    cv2.createTrackbar("Width","Resize Slider",img.shape[1],img.shape[1]*2,lambda x: None)
    cv2.createTrackbar("Height","Resize Slider",img.shape[0],img.shape[0]*2,lambda x: None)
    while True:
        w = cv2.getTrackbarPos("Width","Resize Slider")
        h = cv2.getTrackbarPos("Height","Resize Slider")
        resized = cv2.resize(img,(max(w,1),max(h,1)))
        cv2.imshow("Resize Slider",resized)
        if cv2.waitKey(1)&0xFF == 27:
            cv2.imwrite("resized_slider.jpg",resized)
            speak(f"Image resized to width {w} and height {h}")
            break
    cv2.destroyAllWindows()
    print("✅ Saved resized_slider.jpg")
    return resized

def main_menu():
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
        if choice=="1":
            path=input("Path: "); w=int(input("Width: ")); h=int(input("Height: "))
            img_resized = resize_fixed_cv(path,w,h)
            display_with_matplotlib(cv2.imread(path),img_resized)
        elif choice=="2":
            path=input("Path: "); w=int(input("Width: ")); h=int(input("Height: "))
            resize_fixed_pil(path,w,h)
        elif choice=="3":
            path=input("Path: "); pct=int(input("Percent: "))
            resize_percentage(path,pct)
        elif choice=="4":
            folder=input("Folder: "); w=int(input("Width: ")); h=int(input("Height: "))
            batch_resize(folder,w,h)
        elif choice=="5": gui_file_picker_resize()
        elif choice=="6": gui_opencv_slider()
        elif choice=="0": break
        else: print("❌ Invalid choice")

if __name__=="__main__":
    main_menu()
