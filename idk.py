import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
"""
check out the following modules:
Mahotas
SciKit
numpy
scipy
simpleitk

"""

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
    key = cv2.waitKey(20) #waits for 20ms for keyboard event
    if key == 27: #ESC key
        break
cv2.destroyWindow("Camera")
