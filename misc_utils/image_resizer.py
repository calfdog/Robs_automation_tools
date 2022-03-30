#!/usr/bin/python
""" Description: Useful batch image tool for resizing
    your jpg images in a directory to thumbnail or other size
    Developer: Rob M.
"""
from PIL import Image
import os
import glob

# Add you width and Height
width = 150
height = 150


def resize_images():
    """resizes images and prints list of file names that were resized"""
    file_names = glob.glob(r'images\*.jpg')
    for img in file_names:
        im = Image.open(img)
        # split to file and extension
        f, e = os.path.splitext(img)
        # Resize and anti alias
        im_resize = im.resize((width, height), Image.ANTIALIAS)
        # Save as thumb nail or other
        im_resize.save(f + ' small.jpg', 'JPEG', quality=90)
        print(img, "Done")


resize_images()
