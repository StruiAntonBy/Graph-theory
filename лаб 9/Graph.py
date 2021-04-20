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

    def GreedyColorizationAlgorithm(self):   # Жадный алгоритм раскрашивания
        (S, k, f, result) = ({x for x in range(0, self.InterfaceMatrix.line)}, 0, None, [])
        matrix = self.InterfaceMatrix.copyMatrix()
        for i in range(0, matrix.line):
            matrix.Array[i][i] = 1
        Top = None
        while len(S) != 0:
            if Top is None:
                Top = S.pop()
                (k, C) = (k + 1, {Top})
            G = {j for top in C for j in range(0, matrix.line) if matrix.Array[top][j] == 1}
            (TmpS, TmpC) = (set(S), set(C))
            TmpC.update(G)
            TmpSet = TmpS.difference(TmpC)
            if len(TmpSet) == 0:
                (f, S) = (k, S.difference(C))
                C = [x + 1 for x in C]
                result.append((C, f))
                (Top, C) = (None, None)
            else:
                C.add(TmpSet.pop())
        return result

    def AlgorithmSequentialColoring(self):   # Алгоритм последовательного раскрашивания
        result = dict()
        SetColors = {x for x in range(1, self.InterfaceMatrix.line+1)}
        S = {x for x in range(0, self.InterfaceMatrix.line)}
        Array = {x: set(SetColors) for x in S}
        for x in S:
            k = min(Array[x])
            result[x+1] = k
            for j in range(0, self.InterfaceMatrix.line):
                if self.InterfaceMatrix.Array[x][j] == 1:
                        Array[j].discard(k)
        return result