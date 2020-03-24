class Cercle:
    def __init__(self, rayon):
        self.__rayon = rayon

    def __str__(self):
        return "Cerlce de rayon : "+str(self.__rayon)

    def __add__(self, C):
        return Cercle(self.__rayon+C.__rayon)

    def __lt__(self, C):
        return self.__rayon < C.__rayon

    def __gt__(self, C):
        return self.__rayon > C.__rayon

if __name__ == '__main__':
    C1 = Cercle(2)
    C2 = Cercle(3)
    C3 = C1 + C2
    C4 = C1 < C2
    C5 = C2 > C3

    print(C3)
    print(C4)
    print(C5)
    print(isinstance(C1, Cercle))
    print(isinstance(C2, Cercle))

