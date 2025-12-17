import numpy as np 
def Calc_Image_integral(img):
    rows,cols = img.shape
    ii = np.zeros((rows+1 , cols+1) , np.int32)
    for x in range(rows):
        for y in range(cols):
            ii[x+1 , y+1] = img[x,y] + ii[x,y+1] +ii[x+1,y]- ii[x,y]
    return ii[1: , 1:]

img = np.array([
    [4,5,2,1],
    [0,9,3,2],
    [5,6,8,1],
    [2,3,0,0],
    
] , np.int32)

print(Calc_Image_integral(img))