#!/usr/bin/env python3

import cv2
from scipy import ndimage
# from PIL import Image
# import matplotlib.pyplot as plt
# import numpy as np


def main():
    cv2.namedWindow("Camera")
    vc = cv2.VideoCapture(0)
    if vc.isOpened():  # tries to get first frame
        rval, frame = vc.read()
    else:
        rval = False
    while rval:
        cv2.imshow("cam", frame)
        rval, frame = vc.read()

        # convert input image to grayscale image:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # normalize grayscale image data + apply gaussian blur to reduce noise:
        """
        sigma: standard deviation of kernel
        - sigma set to 1 as pseudo-default -> need to test for optimal value
        """
        norm_gray = gray / 255
        gaus_blurred_img = ndimage.gaussian_filter(norm_gray, sigma=1)

        # use canny edge detector to extract edges:
        """
        thresh1: minimum value threshold
        thresh2: maximum value threshold
        - current values are arbitrary
        """
        edges = cv2.Canny(gaus_blurred_img, thresh1=100, thresh2=200)
        cv2.imshow("edges", edges)

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


if __name__ == "__main__":
    main()
