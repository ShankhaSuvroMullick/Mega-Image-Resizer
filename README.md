# Mega Image Resizer 🖼️

## Description
Mega Image Resizer is a Python program to resize images in multiple ways using **CLI (Command-Line Interface)** or **GUI (Graphical User Interface)**.

It demonstrates:

- **Core Python concepts**  
- **Image processing** using **OpenCV** and **Pillow**  
- **GUI design** using **Tkinter**  
- **Text-to-speech notifications** with `pyttsx3`  
- **Side-by-side image comparison** using `matplotlib`  

---

## 📚 Purpose
The project aims to help you:

- Learn **image processing** in Python  
- Understand **OpenCV vs Pillow** resizing techniques  
- Learn **GUI programming** (Tkinter sliders, file pickers)  
- Use **pyttsx3** for notifications  
- Compare images visually using **matplotlib**  
- Automate **batch resizing**  
- Explore **functions, modules, and classes** step by step  

---

## 📦 Modules & Their Meanings

| Module | Meaning / Use in Programming | Why Used Here |
|--------|----------------------------|---------------|
| `os` | Operating system interface | Read folders and save batch-resized images |
| `cv2` | OpenCV library for image/video processing | Resize images, create sliders GUI |
| `PIL.Image` | Pillow (Python Imaging Library) module | Smooth resizing, open/save images |
| `pyttsx3` | Python text-to-speech library | Speak notifications aloud |
| `tkinter` | Standard Python GUI library | File dialogs, input dialogs |
| `matplotlib.pyplot` | Plotting library | Display images side-by-side for comparison |

---

## ⚙️ Key Concepts Explained

| Term | Meaning |
|------|---------|
| `function` | A block of reusable code performing a task |
| `parameter` | Input value for a function, e.g., width, height |
| `return` | Output of a function |
| `variable` | Named storage for a value, e.g., `img`, `w`, `h` |
| `if / elif / else` | Conditional statements |
| `for` / `while` | Loops to repeat code |
| `list` | Ordered collection of items |
| `string` | Text data, e.g., `"Path: "` |
| `int` | Integer data type |
| `object` | Instance of a class, e.g., `Image.open(...)` |
| `method` | Function attached to an object, e.g., `img.resize(...)` |

---

## 🖥️ Function-by-Function Explanation

### 1️⃣ `speak(text)`
**Purpose:** Converts text to speech

```python
engine = pyttsx3.init()
engine.say(text)
engine.runAndWait()
```

---

### 2️⃣ `resize_fixed_cv(image_path, width, height, output_name)`
**Purpose:** Resize images using OpenCV

```python
img = cv2.imread(image_path)
resized = cv2.resize(img, (width, height))
cv2.imwrite(output_name, resized)
```

---


### 3️⃣ `resize_fixed_pil(image_path, width, height, output_name)`
**Purpose:** Resize using Pillow

```python
img = Image.open(image_path)
resized = img.resize((width, height), Image.ANTIALIAS)
resized.save(output_name)
```
---
