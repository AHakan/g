import os
import numpy as np
import matplotlib.pyplot as plt


def get_jpeg():
    print(os.getcwd())
    print(os.listdir())

    path = os.getcwd()

    jpg_image = [ f for f in os.listdir(path) if f.endswith('.jpg')]
    
    return jpg_image

def rotate(rotate_img):
    new_image = np.zeros((760,475,3), dtype='uint8')
    m, n, k = rotate_img.shape
    for i in range(m):
        for j in range(n):
            temp_1 = rotate_img[i, j]
            new_image[j, i] = temp_1

    return new_image


print(get_jpeg())

image = plt.imread('python.jpg')

print(image)

m, n, k = image.shape

print(m, n, k)

for i in range(m):
    for j in range(n):
        #print(i, j, end=" ")
        temp_1 = image[i, j]
        #print(temp_1)


image_2 = image + 100

plt.subplot(1,3,1)
plt.imshow(image)


plt.subplot(1,3,2)
plt.imshow(image_2)



new_image = np.zeros((760,475,3), dtype='uint8')

new_image = rotate(image)

plt.subplot(1,3,3)
plt.imshow(new_image)
plt.show()



# list_n1 = [1, 'sdfsdfs', 2]
# list_n2 = [2, 'dsddfss', 3]
# print(list_n1 + list_n2)

# # nd asarray
# list_1 = np.asarray([1,2,3,4])
# list_2 = np.asarray([1,2,3,4])
# print(list_1 + list_2)