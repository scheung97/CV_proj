import numpy as np
from scipy import signal as sig

def gauss_blur_filter(frame):
    """
    Creates a gaussian blurred image
    :Param: frame data (type: np.ndarray)
    :Return: None (place holder right now)
    """
    try:
        frame = frame / 255 #normalize image data
        """
        R = frame[:,:,0]
        G = frame[:,:,1]
        B = frame[:,:,2]
        """

        #C_linear
        gray = np.array(0.2989*frame[:,:,0] + 0.587*frame[:,:,1] + 0.114*frame[:,:,2] )#a little darker than the cv2 function

        #convolution to apply gaussian blur
        gaussian_blur = (np.array([[1,4,1],[4,8,4],[1,4,1]])) *(1/28)
        blurred_img = sig.convolve2d(gray, gaussian_blur)

        #edge detection

        return gray, blurred_img
    except TypeError as e:
        print(e)
