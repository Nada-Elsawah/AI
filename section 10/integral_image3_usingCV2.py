import numpy as np
#install OpenCV library firstly => pip install opencv-python
# OpenCv (Open Source Computer Vision Library) 
# = > used for a vast range of computer vision and image processing tasks
import cv2
img = np.array([
    [4,5,2,1],
    [0,9,3,2],
    [5,6,8,1],
    [2,3,0,0],
    
] , dtype='uint8')  #8-bit unsigned integer data type

image_integral = cv2.integral(img)
#image_integral = image_integral[1: , 1:] #remove zeros padding
print(image_integral)