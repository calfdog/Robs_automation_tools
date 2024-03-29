"""
    Description: Visual Test tool using OpenCV for
    taking a snapshot as a baseline and then calling this module to to compare
    the two images
    Modified From: Pyimagesearch.com article by Adrian Rosebrock
    This is a work in progress, I will be adding features in the future
    Developer: Rob Marchetti

    Python Requirements:
    pip install imutils
    pip install scikit-image
    pip install opencv-python
    pip install numpy
    pip install pytesseract

"""

from skimage.metrics import structural_similarity
import imutils
import cv2
import pytesseract




def compare_image(img1, img2):
    # read in images
    imageA = cv2.imread(img1)
    imageB = cv2.imread(img2)

    # Convert both images to grayscale
    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

    # compute the Structural Similarity Index (SSIM) between the two
    # images, ensuring that the difference image is returned
    (score, diff) = structural_similarity(grayA, grayB, full=True)
    diff = (diff * 255).astype("uint8")

    # threshold the difference image, followed by finding contours to
    # obtain the regions of the two input images that differ
    thresh = cv2.threshold(diff, 0, 255,
                           cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    # loop over the contours
    for c in cnts:
        # Get the bounding box of the contour and then draw a green
        # bounding box on both input images

        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(imageA, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.rectangle(imageB, (x, y), (x + w, y + h), (0, 0, 255), 2)
        cv2.putText(imageB, 'Missing', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

    # Display the output images
    cv2.imshow("Original", imageA)
    cv2.imshow("Modified", imageB)
    # waitKey(0) will display the window infinitely until any keypress (it is suitable for image display).
    # Move img to open on the top left
    cv2.moveWindow("Original", 0, 0)
    cv2.moveWindow("Modified", 100, 0)
    cv2.waitKey(0)


# These can be any image
# original image - baseline (sample snapshot)
# This image will be highlights to show what was originally there
img1 = "images/imageA.jpg"

# modified image to simulate show missing areas
img2 = "images/imageB.jpg"
compare_image(img1, img2)

# Press escape to close open image windows
cv2.waitKey(0)
cv2.destroyAllWindows()
