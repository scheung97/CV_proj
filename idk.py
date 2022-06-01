#!/usr/bin/env python3

import cv2
# import numpy as np
import filtering as fil
# from PIL import Image
# import matplotlib.pyplot as plt
"""
check out the following modules:
Mahotas
SciKit
numpy
scipy
simpleitk

"""


# part 1: connect webcam to python
# part 2: handle image processing for detection

cv2.namedWindow("Camera")
vc = cv2.VideoCapture(0)
if vc.isOpened():  # tries to get first frame
    rval, frame = vc.read()
else:
    rval = False
while rval:
    cv2.imshow("cam", frame)
    rval, frame = vc.read()

    """
    converts input image to gray
    """
    # filtering already converts to gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    sigma = 2

    # can remove function call to just use library functions themseslves:
    gauss_blurred_img = fil.gauss_blur_filter(gray, sigma)
    edges = fil.cannyEdgeDetector(gauss_blurred_img, 100, 200)

    key = cv2.waitKey(20)  # waits for 20ms for keyboard event
    if key == 27:  # ESC key
        break

"""
frame == np.ndarray
@TODO:
run vertical and horizontal filter on image data
and detect rectangular objects (street signs, boxes, etc)
"""

# ensures cam resource isn't locked + closes the camera window:
vc.release()
cv2.destroyWindow("Camera")
