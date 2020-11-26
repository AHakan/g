import os
import numpy as np
import matplotlib.pyplot as plt


def get_jpeg():
    print(os.getcwd())
    print(os.listdir())

    path = os.getcwd()

    jpg_image = [ f for f in os.listdir(path) if f.endswith('.jpg')]
    
    return jpg_image

def convert_rgb_to_gray_level(im_1):
    m=im_1.shape[0]
    n=im_1.shape[1]
    im_2=np.zeros((m,n))
    for i in range(m):
        for j in range(n):
            im_2[i,j] = get_distance(im_1[i,j,:])
    
    return im_2

def get_distance(v,w=[1/3,1/3,1/3]):
    a,b,c = v[0], v[1], v[2]
    w1,w2,w3 = w[0],w[1],w[2]
    d = ((a**2)**w1 +
    (b**2)*w2+
    (c**2)*w3)**.5

    return d

def get_mask_for_edge():
    return np.array([-1,0,1,-2,0,2,-1,0,1]).reshape(3,3)
      
def apply_mask_for_edge(part_of_image):
    mask = get_mask_for_edge()
    return sum(sum(part_of_image*mask))

def get_edges(im_1):
    m=im_1.shape[0]
    n=im_1.shape[1]
    im_2=np.zeros((m,n))
    
    for i in range(3,m-3):
        for j in range(3, n-3):
            poi=im_1[i-1:i+2, j-1:j+2]

            im_2[i,j] = apply_mask_for_edge(poi)
    
    return im_2


poi_1 = get_mask_for_edge()

print(apply_mask_for_edge(poi_1))


im_1 = plt.imread(get_jpeg()[0])
plt.subplot(1,3,1)
plt.imshow(im_1)

im_2 = convert_rgb_to_gray_level(im_1)
plt.subplot(1,3,2)
plt.imshow(im_2, cmap='gray')

im_3 = get_edges(im_2)
plt.subplot(1,3,3)
plt.imshow(im_3, cmap='gray')

plt.show()

