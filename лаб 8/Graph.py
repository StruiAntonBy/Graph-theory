class Graph:

    def __init__(self, matrix):
        self.InterfaceMatrix = matrix  # Матрица смежности

    def getAllRibs(self):   # Возврощает все ребра
        AllRibs = []
        for i in range(0, self.InterfaceMatrix.line):
            for j in range(0, self.InterfaceMatrix.column):
                if self.InterfaceMatrix.Array[i][j] == 1:
                    AllRibs.append((i, j))
        return AllRibs

    def oriented(self):   # Орграф
        for i in range(0, self.InterfaceMatrix.line):
            for j in range(0, self.InterfaceMatrix.line):
                if self.InterfaceMatrix.Array[i][j] == 1 and self.InterfaceMatrix.Array[j][i] == 1:
                    return False
                elif self.InterfaceMatrix.Array[i][j] == 1 and self.InterfaceMatrix.Array[j][i] != 1:
                    return True

    def print_InterfaceMatrix(self):
        self.InterfaceMatrix.show_matrix()

    def searchWidth(self, NumberTop):
        queue = [NumberTop - 1]
        ArrayMark = {NumberTop: 0}
        while len(queue) != 0:
            NumberTop = queue.pop(0)
            ArrayMark = self.__SearchWidthAlgorithm(NumberTop, ArrayMark[NumberTop + 1], ArrayMark, queue)
        return ArrayMark

    def getWay(self, TopStrart, TopEnd):
        ArrayMark = self.searchWidth(TopStrart)
        if TopStrart == TopEnd:
            return [TopStrart]
        elif list(ArrayMark.keys()).count(TopEnd) == 1:
            Way = [TopEnd]
            Mark = ArrayMark[TopEnd]
            while Mark != 0:
                Mark = Mark-1
                for key in ArrayMark.keys():
                    if ArrayMark[key] == Mark and self.InterfaceMatrix.Array[key-1][Way[len(Way)-1]-1] == 1:
                        Way.append(key)
                        break
            Way.reverse()
            return Way
        else:
            return None

    def __SearchWidthAlgorithm(self, NumberTop, Mark, ArrayMark, queue):
        Mark = Mark + 1
        for j in range(0, self.InterfaceMatrix.column):
            if self.InterfaceMatrix.Array[NumberTop][j] == 1 and list(ArrayMark.keys()).count(j + 1) == 0:
                ArrayMark[j + 1] = Mark
                queue.append(j)
        return ArrayMark

    def bipartite(self):  # Двудольный граф
        ArrayMark = self.searchWidth(1)
        V1 = []
        V2 = []
        for x in ArrayMark.keys():
            if ArrayMark[x] % 2 == 0:
                V2.append(x - 1)
            else:
                V1.append(x - 1)
        for i in V1:
            for j in V1:
                if j == i:
                    continue
                elif self.InterfaceMatrix.Array[i][j] == 1:
                    return False
        for i in V2:
            for j in V2:
                if j == i:
                    continue
                elif self.InterfaceMatrix.Array[i][j] == 1:
                    return False
        return True