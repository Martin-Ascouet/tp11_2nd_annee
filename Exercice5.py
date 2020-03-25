class Matrice:
    def __init__(self, data):
        self.__data = data

    def __str__(self):
        return "|"+str(self.__data[0][0])+" "+str(self.__data[0][1])+"|\n|"+str(self.__data[1][0])+" "+str(self.__data[1][1])+"|"

    def __add__(self, M):
        a = ([self.__data[0][0] + M.__data[0][0], self.__data[0][1] + M.__data[0][1]],[self.__data[1][0] + M.__data[1][0], self.__data[1][1] + M.__data[1][1]])
        return Matrice(a)

    def __sub__(self, M):
        a = ([self.__data[0][0] - M.__data[0][0], self.__data[0][1] - M.__data[0][1]],[self.__data[1][0] - M.__data[1][0], self.__data[1][1] - M.__data[1][1]])
        return Matrice(a)

if __name__ == "__main__":
    M1 = Matrice(([2, 1], [3, 2]))
    M2 = Matrice(([3, 4], [5, 6]))
    M3 = M1 - M2
    M4 = M1 + M2
    print(M3)
    print(M4)
