import cv2
import numpy as np

def scale_range (input, min, max):
    input += -(np.min(input))
    input /= np.max(input) / (max - min)
    input += min
    return input

#the darker regions have higher concentration of green pigment
def green_leaf_index(r,g,b):
    top=2*g-r-b
    down=2*g+r+b
    down[down == 0] = 1
    temp = top/down
    scaled = scale_range(temp, 0, 255)
    return temp,scaled

def summed_green_reflectance(g):
    return sum(g)

def vi_green(g,r):
    top= g-r
    down= g+r
    down[down == 0] = 1
    temp = temp = top/down
    scaled = scale_range(temp, 0, 255)
    return temp,scaled

#darker regions have more foliage coverage
def red_to_green_ratio(r,g):
    g[g==0] = 225*100
    scaled = scale_range(r/g, 0, 255)
    return r/g, np.array(scaled, dtype = np.uint8 )

def read_image(name):
    image = cv2.imread(name)
    return image

'''
(1/R510) - (1/R550)
'''
def carotenoid_reflectance_index_550(g):
    range_500

'''
(R550 - R450)/(R550 + R450)
'''
def plant_pigment_ratio(g):
    range_450_500


'''
NExG: Normalized Excess Green Index
 (2*G−R−B)/(G + R + B) 
'''
def normalized_excess_green_index(r,g,b):
    top = (2*g - r - b)
    down = (g + r + b)
    down[down == 0] = 1
    temp = top / down
    scaled = scale_range(temp, 0, 255)
    temp, scaled

'''
NGRDI: Normalized green-red difference index 
  (G - R)/ (G + R)
'''
def normalized_green_red_diff_index(r,g,b):
    top = (g - r)
    down = (g + r)
    down[down == 0] = 1
    temp = top / down
    scaled = scale_range(temp, 0, 255)
    temp, scaled


def split_rgb(img):
    red = img[:,:,2]
    green = img[:,:,1]
    blue = img[:,:,0]
    return red, green, blue

def display(img):
    cv2.imshow("",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def avg(arr):
    return np.average(arr)

#-----------calculating indexes----------------- 

r,g,b = split_rgb(read_image("1.png"))

glf,scaled_glf = green_leaf_index(r, g, b)
#print(avg(glf))
#display(scaled_glf)

VIgreen,VIgreen_sclaed = vi_green(g,r)
#print(avg(VIgreen))
#display(VIgreen_sclaed)

r_to_g, r_to_g_scaled = red_to_green_ratio(r,g)
#print(avg(r_to_g))
#display(r_to_g_scaled)

sgr = summed_green_reflectance(g)
            