import os
import numpy as np
import matplotlib.pyplot as plt


def get_jpeg():
    print(os.getcwd())
    print(os.listdir())

    path = os.getcwd()

    jpg_image = [ f for f in os.listdir(path) if f.endswith('.jpg')]
    
    return jpg_image


img_0 = plt.imread(get_jpeg()[0])


# x = np.array(list(range(100)))
# y = np.sin(np.array(list(range(100))))
# plt.subplot(4,5,1)
# plt.plot(x,y)


# y = 1/(1+np.exp(x))
# plt.subplot(4,5,2)
# plt.plot(x,y)


# y = np.power(x/float(np.max(x)), 1)

# plt.subplot(4,5,3)
# plt.plot(x,y)


# y_2 = np.power(x/float(np.max(x)), 1/10)
# y_3 = np.power(x/float(np.max(x)), 10)

# plt.subplot(4,5,4)
# plt.plot(x,y)
# plt.plot(x,y_2)
# plt.plot(x,y_3)

# plt.show()


img_100 = np.power(img_0/float(np.max(img_0)), 1/10)
plt.imshow(img_100)

plt.show()



