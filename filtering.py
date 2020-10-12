import numpy as np

def filtering(frame):
    """
    Creates filtered image for processing
    :Param: frame data (type: np.ndarray)
    :Return: None (place holder right now)
    """

    #TODO: fix IndexError

    #RGB --> Gray conversion: https://stackoverflow.com/questions/17615963/standard-rgb-to-grayscale-conversion
    try:
        frame = frame / 255 #normalize image data
        """
        R = frame[:,:,0]
        G = frame[:,:,1]
        B = frame[:,:,2]
        """

        #C_linear
        gray = np.array(0.2126*frame[:,:,0] + 0.7152*frame[:,:,1] + 0.0722*frame[:,:,2] )#a little darker than the cv2 function

        #C_sRGB --> should be grayscale
        gray_row = len(gray[:,0])
        gray_col = len(gray[0,:])
        #gray[x][y] <= val
        #only integer scalar arrays can be converted to a scalar index --> need to adjust indices to account for it being an np.array()
        i, j = np.indices((gray_row, gray_col)) #i = rows; j = cols
        for x in range(0,1):
            for y in range(0, 1):
                if gray[x,y] <= 0.0031308: #if just "gray" --> ValueError: The truth value of an array with more than one element is ambiguous. Use a.any() or a.all()
                    gray_but_better[x,y] = 12.92*gray[x,y]
                else:
                    gray_but_better[x,y] = (1.055*(gray[x,y]**(1/2.4))) - 0.055
        return gray_but_better
    except TypeError as e:
        print(e)
