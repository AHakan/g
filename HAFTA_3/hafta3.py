import os
import numpy as np
import matplotlib.pyplot as plt


def get_jpeg():
    print(os.getcwd())
    print(os.listdir())

    path = os.getcwd()

    jpg_image = [ f for f in os.listdir(path) if f.endswith('.jpg')]
    
    return jpg_image


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

image = plt.imread(get_jpeg()[0])

m, n, k = image.shape #[row,col,rgb]

#print(image.ndim)

im_2 = convert_rgb_to_gray(image)

plt.imsave('python_blue.jpg', im_2)
plt.imsave('python_gray.jpg', im_2, cmap='gray')

plt.subplot(1,3,1)
plt.imshow(image)
plt.subplot(1,3,2)
plt.imshow(im_2)
plt.subplot(1,3,3)
plt.imshow(im_2, cmap='gray')
plt.show()



