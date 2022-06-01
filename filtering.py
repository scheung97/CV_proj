import numpy as np
import cv2
from scipy import signal as sig
from scipy import ndimage 

def gauss_blur_filter(frame, sigma):
    """
    Creates a gaussian blurred image to smooth the image
    :Param: gray-scale frame data (type: np.ndarray)
    :Return: None (place holder right now)
    """

    #size of this filter will impact the detector

    try:
        frame = frame / 255 #normalize image data
        """
        R = frame[:,:,0]
        G = frame[:,:,1]
        B = frame[:,:,2]
        """

        # #convolution to apply gaussian blur (math approach):
        # gaussian_blur = (np.array([[1,4,1],[4,8,4],[1,4,1]])) *(1/28)  #maybe increase the size to decrease effects of noise
        # blurred_img = sig.convolve2d(frame, gaussian_blur)

        #gauss blurring using library function: 
        blurred_img = ndimage.gaussian_filter(frame, sigma) #sigma value modified in idk.py

        return blurred_img
    except TypeError as e:
        print(e)
"""
def horizontal_filter(frame):
    ''''
    Creates horizontal filter that detects horizontal lines
    :Param: frame data (type: np.ndarray)
    :Return: None (place holder right now)
    '''
    #horizontal_filter = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
    #horizontal_filter = (np.array([[1,1,1],[0,0,0],[-1,-1,-1]]))*(1/6) #prewit operator
    horizontal_filter = (np.array([[1,2,1],[0,0,0],[-1,-2,-1]]))*(1/4) #sobel operator

    filtered_image = sig.convolve2d(frame, horizontal_filter)
    return filtered_image

def vertical_filter(frame):
    '''
    Creates vertical filter that detects vertical lines
    :Param: frame data (type: np.ndarray)
    :Return: None (place holder right now)
    '''

    #vertical_filter = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
    #vertical_filter = (np.array([[-1,0,1],[-1,0,1],[-1,0,1]]))*(1/6) #prewitt operator
    vertical_filter = (np.array([[-1,0,1],[-2,0,2],[-1,0,1]]))*(1/4) #sobel operator

    filtered_image = sig.convolve2d(frame, vertical_filter)
    return filtered_image
"""

#Canny Edge Detector
def cannyEdgeDetector(frame, thresh1, thresh2):

    # ############################################################################
    # #Horizontal Sobel filter
    # ############################################################################

    # #horizontal_filter = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
    # #horizontal_filter = (np.array([[1,1,1],[0,0,0],[-1,-1,-1]]))*(1/6) #prewit operator
    # horizontal_filter = (np.array([[1,2,1],[0,0,0],[-1,-2,-1]]))*(1/4) #sobel operator

    # horizontal = sig.convolve2d(frame, horizontal_filter)

    # ############################################################################
    # #Vertical Sobel filter
    # ############################################################################

    # #vertical_filter = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
    # #vertical_filter = (np.array([[-1,0,1],[-1,0,1],[-1,0,1]]))*(1/6) #prewitt operator
    # vertical_filter = (np.array([[-1,0,1],[-2,0,2],[-1,0,1]]))*(1/4) #sobel operator

    # vertical = sig.convolve2d(frame, vertical_filter)

    # ############################################################################
    # #Find Intensity Gradients
    # ############################################################################
    # magnitude = np.sqrt((horizontal**2)+(vertical**2))
    # direction = np.arctan(vertical/horizontal)

    # ############################################################################
    # #Non-maximum Supression
    # ############################################################################

    #Canny Edge Detection using OpenCV
    edges = cv2.Canny(frame, thresh1, thresh2) #threshold values modified in idk.py
    return edges
