import math as mt
class Complex:
    def __init__(self, re, im):
        self.__re = re
        self.__im = im

    def __str__(self):
        return str(self.__re)+"+"+"i"+str(self.__im)

    def __add__(self, C):
        return Complex(self.__re+C.__re, self.__im+C.__im)

    def __sub__(self, C):
        return Complex(self.__re-C.__re, self.__im-C.__im)

    def __mul__(self, C):
        return Complex(self.__re*C.__re +-self.__im*C.__im, self.__im*C.__re + self.__re*C.__im)

    def __truediv__(self, C):
        return Complex((self.__re*C.__re +self.__im*C.__im)/(C.__re**2+C.__im**2), (self.__im*C.__re + self.__re*-C.__im)/(C.__re**2+C.__im**2))

    def __abs__(self):
        return mt.sqrt(self.__re**2+self.__im**2)

    def __eq__(self, C):
        return self.__re == C.__re and self.__im == self.__im

    def __ne__(self, C):
        return self.__re != C.__re or self.__im != C.__im

if __name__ == '__main__':
    C1 = Complex(2, 3)
    C2 = Complex(4, 2)
    C3 = C1 + C2
    C4 = C1 - C2
    C5 = C1 * C2
    C6 = C1 / C2
    C7 = abs(C1)

    print("C1 + C2 =",C3)
    print("C1 - C2 =",C4)
    print("C1 * C2 =",C5)
    print("C1 / C2 =",C6)
    print("|C1| =", C7)
    print(C1 == C2)
    print(C1 != C2)



