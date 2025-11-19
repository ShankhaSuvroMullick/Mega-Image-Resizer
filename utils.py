# utils.py
from PIL import Image
import cv2
import matplotlib.pyplot as plt

def display_with_matplotlib(original, resized):
    """
    Display original and resized images side-by-side.
    """
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
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
