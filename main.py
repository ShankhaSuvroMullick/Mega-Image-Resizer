# main.py
from resize_cv import resize_fixed_cv
from resize_pil import resize_fixed_pil, resize_percentage, batch_resize
from gui import gui_file_picker_resize, gui_opencv_slider
from utils import display_with_matplotlib
import cv2

def main_menu():
    """
    Main CLI menu for Mega Image Resizer.
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

if __name__ == "__main__":
    main_menu()
