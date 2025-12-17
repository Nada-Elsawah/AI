import numpy as np
#compute the integral image with zero padding
import numpy as np 
def Calc_Image_integral(img):
    rows,cols = img.shape
    ii = np.zeros((rows+1 , cols+1) , np.int32)
    for x in range(rows):
        for y in range(cols):
            ii[x+1 , y+1] = img[x,y] + ii[x,y+1] +ii[x+1,y]- ii[x,y]
    return ii[1: , 1:]

#compute the sum of Subregion using integral image
def IIsumRegion(IntImage , x,y,w,h):
    """
    x,y => top-left coordinate (row, columns)
    w,h => weight - hight of region
    """
    regionSum = IntImage[y+h-1 , x+w-1] - IntImage[y-1 , x+w-1] - IntImage[y+h-1 , x-1] +IntImage[y-1 , x-1]
    return regionSum

img = np.array([
    [4,5,2,1],
    [0,9,3,2],
    [5,6,8,1],
    [2,3,0,0],
    
] , np.int32)
ImageIntegral = Calc_Image_integral(img)
print("Image Integral \n" , ImageIntegral)
region_sum = IIsumRegion(ImageIntegral , 1,1,3,2)
print("Sum of Subregion :" , region_sum)


