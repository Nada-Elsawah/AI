import numpy as np
def integral_image(img):
    rows,cols=len(img),len(img[0])
    ii = np.zeros((rows,cols), np.int32) #ii => integral image (initialize a matrix row*col contains zeros value)
    for x in range(rows):
        for y in range(cols):
            Upper_pixel = ii[x-1][y] if x >0 else 0
            Left_pixel = ii[x][y-1] if y>0 else 0
            Upper_Left_pixel = ii[x-1][y-1] if (x>0 and y > 0) else 0
            ii[x][y]= img[x][y] + Upper_pixel + Left_pixel - Upper_Left_pixel
    return ii

img = [
    [4,5,2,1],
    [0,9,3,2],
    [5,6,8,1],
    [2,3,0,0]
]

print(np.array(integral_image(img)))
    