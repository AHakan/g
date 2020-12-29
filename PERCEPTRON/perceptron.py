import numpy as np

class Perceptron(object):
    # baslangic degerlerini atiyor.
    def __init__(self, input_size, lr=1, epochs=10):
        self.W = np.zeros(input_size+1)

        self.epochs = epochs
        self.lr = lr

    # aktivasyon işlemi uygular. giriş degeri 0 dan buyukse ve eşitse 1 degilse 0 donduruyor.
    def activation_fn(self, x):
        return 1 if x >=0 else 0

    # transpoze alır ve tek değer üretir bunu activasyona gonderir.
    def predict(self, x):
        x = np.insert(x, 0, 1)
        z = self.W.T.dot(x)
        a = self.activation_fn(z)
        print(a)
        return a

    # verilen değerin transpozesini alıp bunu kapıdan çıkartıyor ve değerleri olusturuyor.
    def fit(self, X, d):
        for _ in range(self.epochs):
            for i in range(d.shape[0]):
                y = self.predict(X[i])
                e = d[i] - y
                self.W = self.W + self.lr * e * np.insert(X[i], 0, 1)

# mp = Perceptron(5)

# x = np.asarray([1,2,3,4,5])

# print(mp.predict(x))


X = np.array([[0,0], [0, 1], [1, 0], [1, 1]])

d = np.array([0, 0, 0, 1])

perceptron = Perceptron(input_size=2)

perceptron.fit(X, d)

print(perceptron.W)


# 1.sorunun cevabı fonksiyonlar üzerinde yazıyor.


# 2.sorunun cevabı olarak XOR => d = np.array([0, 1, 1, 0])
#  [ 0. -1.  0.] sonucu dönüyor.


# 3.soru

# imza tanılaması için girilen imza dataları siyah ve beyaz dönüşümü yapılıp kullanılabilir dersek dizi:
# [[ 1 1 1 .... 1 1 1 1]
#  [ 0 0 0 .... 0 0 0 0]
#  [ 1 0 0 .... 0 1 0 0]
#  ....
#  ....
# ] gibi olacaktır.

# bundan dolayı X = np.asarray([[[ 1 1 1 .... 1 1 1 1]
#  [ 0 0 0 .... 0 0 0 0]
#  [ 1 0 0 .... 0 1 0 0]
#  ....
#  ....
# ]])

# d = np.array([0, 0, 0, 1])

# d yi de and kapısı seçersek verilerin dot çarpımları yapıldıktan sonra her imza için predict fonksiyonu ile farklı bi değer bulunur.
# bu saye de her imza için farklı değerler oluşturulur.

# 4.soru 
# bu modelin hatası XOR gibi ilnearly separable olmayan veriler için sıkıntı oluşturur. bu veriler de doğru sonucu elde edemeyebiliriz.