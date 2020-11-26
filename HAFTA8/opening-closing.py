import os
import numpy as np
import matplotlib.pyplot as plt


def get_jpeg():
    print(os.getcwd())
    print(os.listdir())

    path = os.getcwd()

    jpg_image = [ f for f in os.listdir(path) if f.endswith('.png')]

    return jpg_image

def convert_RGB_to_monochrome_BW(img_1, threshold=0.5):
    img_2 = np.zeros((img_1.shape[0], img_1.shape[1]))
    for i in range(img_2.shape[1]):
        for j in range(img_2.shape[1]):
            if(img_1[i,j,0]/3+img_1[i,j,1]/3+img_1[i,j,1]/3)>threshold:
                img_2[i,j] = 1
            else:
                img_2[i,j] = 0
    return img_2

def define_mask_1():
    mask_1 = [[1,1,1], [1,1,1], [1,1,1]]

    return mask_1

def define_mask_2():
    mask_1 = [[0,0,0], [0,0,0], [0,0,0]]


    return mask_1

def my_dilation(img_1, mask, morphologyOperation='dilation'):
    m = img_1.shape[0]
    n = img_1.shape[1]
    img_2=np.zeros((m,n), dtype='uint8')
    for i in range(1, m-1):
        for j in range(1, n-1):

            x_1 = img_1[i,j] == mask[1][1]

            x_2 = img_1[i-1,j-1] == mask[0][0]
            x_3 = img_1[i-1,j] == mask[0][1]
            x_4 = img_1[i-1,j+1] == mask[0][2]

            x_5 = img_1[i+1,j-1] == mask[2][0]
            x_6 = img_1[i+1,j] == mask[2][1]
            x_7 = img_1[i+1,j+1] == mask[2][2]
            
            x_8 = img_1[i,j-1] == mask[1][0]
            x_9 = img_1[i,j+1] == mask[1][2]
            
            
            if(morphologyOperation=='dilation'):
                result_1 = x_1.any() or x_2.any() or x_3.any() or x_4.any() or x_5.any()
                result_2 = x_6.any() or x_7.any() or x_8.any() or x_9.any()

                result = result_1 or result_2
            
            elif(morphologyOperation=='erosion'):
                result_1 = x_1.any() and x_2.any() and x_3.any() and x_4.any() and x_5.any()
                result_2 = x_6.any() and x_7.any() and x_8.any() and x_9.any()

                result = result_1 and result_2

            img_2[i,j] = result
    
    return img_2
            
def m_f_0_and(l1,l2):
    s = []
    for i in range(len(l1)):
        s.append(l1[i] and l2[i])
    return s


def m_f_1_AND_or_OR(l1, operator=0):
    if operator:
        if 1 in l1:
            s1 = 1
        else:
            s1=0
    else:
        if 0 in l1:
            s1 = 0
        else:
            s1=1

    return s1

def m_f_2_combine(l1,l2, op=0):
    a = m_f_0_and(l1,l2)
    return m_f_1_AND_or_OR(a,op)




img_1 = plt.imread(get_jpeg()[0])
plt.subplot(1,3,1)
plt.imshow(img_1)

img_2 = my_dilation(img_1, define_mask_1(), 'erosion')         # opening operation
img_3 = my_dilation(img_2, define_mask_1(), 'erosion')
img_4 = my_dilation(img_3, define_mask_1(), 'erosion')

img_5 = my_dilation(img_4, define_mask_1(), 'dilation')
img_6 = my_dilation(img_5, define_mask_1(), 'dilation')
img_7 = my_dilation(img_6, define_mask_1(), 'dilation')


plt.subplot(1,3,2)
plt.imshow(img_7, cmap='gray')

img_21 = my_dilation(img_1, define_mask_1(), 'dilation')         # closing operation
img_31 = my_dilation(img_21, define_mask_1(), 'dilation')
img_41 = my_dilation(img_31, define_mask_1(), 'dilation')

img_51 = my_dilation(img_41, define_mask_1(), 'erosion')
img_61 = my_dilation(img_51, define_mask_1(), 'erosion')
img_71 = my_dilation(img_61, define_mask_1(), 'erosion')

plt.subplot(1,3,3)
plt.imshow(img_71, cmap='gray')

plt.show()
