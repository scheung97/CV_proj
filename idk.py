#!/usr/bin/env python3

import cv2
import numpy as np
import filtering as fil
#from PIL import Image
#import matplotlib.pyplot as plt
"""
check out the following modules:
Mahotas
SciKit
numpy
scipy
simpleitk

"""


import nms
#part 1: connect webcam to python
#part 2: handle image processing for detection

cv2.namedWindow("Camera")
vc = cv2.VideoCapture(0)
if vc.isOpened(): #tries to get first frame
    rval, frame = vc.read()
else:
    rval = False
while rval:
    cv2.imshow("cam", frame)
    rval, frame = vc.read()

    """
    converts input image to gray
    """
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  #filtering already converts to gray

    gauss_blurred_img = fil.gauss_blur_filter(gray)
    magnitude, phase = fil.cannyEdgeDetector(gauss_blurred_img)

    max = nms.maximum(magnitude,phase) #very slow

    #cv2.imshow("blur", gauss_blurred_img) #keeping to check if input img is blurred enough
    cv2.imshow("mag", magnitude)
    #cv2.imshow("direction", phase)
    cv2.imshow("max", max)

    key = cv2.waitKey(20) #waits for 20ms for keyboard event
    if key == 27: #ESC key
        break

"""
frame == np.ndarray
@TODO: run vertical and horizontal filter on image data to detect rectangular objects (street signs, boxes, etc)
"""

#ensures cam resource isn't locked + closes the camera window:
vc.release()
cv2.destroyWindow("Camera")
