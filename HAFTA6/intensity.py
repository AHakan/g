import os
import numpy as np
import matplotlib.pyplot as plt


def get_jpeg():
    print(os.getcwd())
    print(os.listdir())

    path = os.getcwd()

    jpg_image = [ f for f in os.listdir(path) if f.endswith('.jpg')]
    
    return jpg_image

def my_f_1(a,b):
    if(a<=255-b):
        return a+b
    else:
        return a

def my_f_2(a):
    return int(255-a)

def get_value_from_triple(temp_1):
    return int(temp_1[0]/3+temp_1[1]/3+temp_1[2]/3)

def convert_rgb_to_gray(image):

    m, n, k = image.shape

    new_image = np.zeros((m,n), dtype='uint8')

    for i in range(m):
        for j in range(n):
            temp_1 = image[i,j,:]
            s=get_value_from_triple(temp_1)
            new_image[i,j]=s
    
    return new_image

img_0 = plt.imread(get_jpeg()[0])

img_1 = convert_rgb_to_gray(img_0)

m, n = img_1.shape

img_3 = np.zeros((m,n), dtype='uint8')

for i in range(m):
    for j in range(n):
        intensity = img_1[i,j]
        increment = 100
        img_3[i,j] = my_f_1(intensity, increment)

img_4 = np.zeros((m,n), dtype='uint8')

for i in range(m):
    for j in range(n):
        intensity = img_1[i,j]
        img_4[i,j] = my_f_2(intensity)


plt.subplot(1,4,1)
plt.imshow(img_0)
plt.subplot(1,4,2)
plt.imshow(img_1, cmap = "gray")
plt.subplot(1,4,3)
plt.imshow(img_3, cmap = "gray")

plt.subplot(1,4,4)
plt.imshow(img_4, cmap = "gray")

plt.show()

#print(img_0.ndim, img_0.shape)
# print(img_1.ndim, img_1.shape)