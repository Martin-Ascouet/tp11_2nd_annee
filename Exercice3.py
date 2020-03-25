class Rational:
    def __init__(self, num, den):
        self.__num = num
        self.__den = den

    def pgcd(self, F):
        a = self.__num * F.__den + self.__den * F.__num
        b = self.__den * F.__den
        r = a % b
        while r != 0 and b != 0:
            a = b
            b = r
            r = a % b
        return b

    def __str__(self):
        return str(self.__num) + "/" + str(self.__den)

    def __add__(self, F):
        b = self.pgcd(F)
        return Rational((self.__num * F.__den + self.__den * F.__num) / b, self.__den * F.__den / b)

    def __sub__(self, F):
        return Rational((self.__num * F.__den - self.__den * F.__num), self.__den * F.__den)

    def __eq__(self, F):
        return self.__num/self.__den == F.__num/F.__den

    def __ne__(self, F):
        return self.__num/self.__den != F.__num/F.__den

if __name__ == '__main__':
    F1 = Rational(8, 9)
    F2 = Rational(5,4)
    F3 = F1 + F2
    F4 = F1 - F2
    F5 = F1 == F2
    F6 = F1 != F2
    print("F1 + F2 = ",F3)
    print("F1 - F2 = ",F4)
    print("F1 = F2 :",F5)
    print("F1 != F2 :",F6)
    print(isinstance(F2, Rational))
    print(isinstance(F2, Rational))
