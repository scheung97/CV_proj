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
    own = fil.filtering(frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("gray", gray)
    cv2.imshow("own", own)
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
