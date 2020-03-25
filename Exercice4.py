class Duree:
    def __init__(self, heure, minute, seconde):
        self.__heure = heure
        self.__minute = minute
        self.__seconde = seconde

    def __str__(self):
        if self.__seconde >= 60:
            a = self.__seconde%60
            b = self.__seconde//60
            self.__minute += b
            self.__seconde = a

        if self.__minute >= 60:
            a = self.__minute%60
            b = self.__minute//60
            self.__heure += b
            self.__minute = a

        return str(self.__heure)+"h"+str(self.__minute)+"m"+str(self.__seconde)+"s"

    def __add__(self, D):
        return Duree(self.__heure+D.__heure, self.__minute+D.__minute, self.__seconde+D.__seconde)

if __name__ == "__main__":
    D1 = Duree(2,59,60)
    D2 = Duree(3, 20, 61)
    D3 = D1 + D2
    print(D1)
    print(D3)
