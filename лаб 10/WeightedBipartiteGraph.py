from BipartiteGraph import BipartiteGraph
from Matrix import Matrix

class WeightedBipartiteGraph(BipartiteGraph):   # Двудольный взвешенный граф
                                                # Матрица весов бесконечность = $
    def __init__(self, WeightMatrix):
        self.WeightMatrix = WeightMatrix   # Матрица весов
        self.__bipartite()
        self.InterfaceMatrix = Matrix()
        self.InterfaceMatrix.initializeMatrix(WeightMatrix.line+WeightMatrix.column, WeightMatrix.line+WeightMatrix.column)
        for i in self.V1:
            for j in range(0, WeightMatrix.column):
                if self.WeightMatrix.Array[i][j] != '$':
                    self.InterfaceMatrix.Array[i][WeightMatrix.line + j] = 1
                    self.InterfaceMatrix.Array[WeightMatrix.line + j][i] = 1

    def __bipartite(self):
        self.V1 = [x for x in range(0, self.WeightMatrix.line)]
        self.V2 = [x for x in range(self.WeightMatrix.line, self.WeightMatrix.line + self.WeightMatrix.column)]

    def print_WeightMatrix(self):
        self.WeightMatrix.show_matrix()

    def PerfectMatchMinimumWeight(self):   # Проверяет существования совершенное паросочетание минимального веса
        if len(self.getLargestMatch()) == self.WeightMatrix.line and self.WeightMatrix.line == self.WeightMatrix.column:
            return True
        else:
            return False

    def getPerfectMatchMinimumWeight(self):   # Совершенное паросочетание минимального веса
        if self.PerfectMatchMinimumWeight():
            matrix = self.WeightMatrix.copyMatrix()
            for line in matrix.Array:
                tmpLine = [x for x in line if x != '$']
                MinElement = min(tmpLine)
                for j in range(0, len(line)):
                    if line[j] != '$':
                        line[j] = line[j] - MinElement
            for j in range(0, matrix.column):
                tmpColumn = [matrix.Array[x][j] for x in range(0, matrix.line) if matrix.Array[x][j] != '$']
                MinElement = min(tmpColumn)
                i = 0
                while i < matrix.line:
                    if matrix.Array[i][j] != '$':
                        matrix.Array[i][j] = matrix.Array[i][j] - MinElement
                    i = i + 1
            InterfaceMatrix = Matrix()
            N = matrix.line + matrix.column
            InterfaceMatrix.initializeMatrix(N, N)
            V1 = [x for x in range(0, matrix.line)]
            V2 = [x for x in range(matrix.line, N)]
            for i in V1:
                for j in range(0, matrix.column):
                    if matrix.Array[i][j] != '$' and matrix.Array[i][j] == 0:
                        InterfaceMatrix.Array[i][matrix.line + j] = 1
                        InterfaceMatrix.Array[matrix.line + j][i] = 1
            graph = BipartiteGraph(InterfaceMatrix, V1, V2)
            P = graph.getLargestMatch()
            Xp = []
            Yp = []
            for i in range(0, len(P)):
                tmp = P[i]
                Xp.append(tmp[0] - 1)
                Yp.append(tmp[1] - 1)
                P[i] = (tmp[0] - 1, tmp[1] - 1)
            tmpV1 = [x for x in V1 if Xp.count(x) == 0]
            tmpV2 = [y for y in V2 if Yp.count(y) == 0]
            if len(tmpV1) == len(tmpV2) and len(tmpV1) == 0:
                P = [(x[0]+1, x[1] - len(graph.V1) + 1) for x in P]
                Sum = 0
                for x in P:
                    Sum = Sum + self.WeightMatrix.Array[x[0] - 1][x[1] - 1]
                return P, Sum
            else:
                RibsIgnore = []
                for rib in P:
                    graph.InterfaceMatrix.Array[rib[0]][rib[1]] = 0
                    RibsIgnore.append((rib[1], rib[0]))
                AllRibs = graph.getAllRibs()
                for rib in AllRibs:
                    if RibsIgnore.count(rib) == 0:
                        if graph.V1.count(rib[0]) == 0:
                            graph.InterfaceMatrix.Array[rib[0]][rib[1]] = 0
                P = self.__getPerfectMatchMinimumWeightAlgorithm(matrix, graph, Xp, Yp, P)
                P = [(x[0] + 1, x[1] - len(graph.V1) + 1) for x in P]
                Sum = 0
                for x in P:
                    Sum = Sum + self.WeightMatrix.Array[x[0] - 1][x[1] - 1]
                return P, Sum
        else:
            return None

    def __getPerfectMatchMinimumWeightAlgorithm(self, matrix, graph, Xp, Yp, P):
        Way = None
        tmpV1 = [x for x in graph.V1 if Xp.count(x) == 0]
        tmpV2 = [y for y in graph.V2 if Yp.count(y) == 0]
        for x in tmpV1:
            flag = False
            for y in tmpV2:
                Way = graph.getWay(x + 1, y + 1)
                if Way is not None:
                    flag = True
                    break
            if flag:
                break
        if Way is not None:
            Way = [x-1 for x in Way]
            i = 1
            while i < len(Way)-1:
                if P.count((Way[i+1], Way[i])) != 0:
                    P.remove((Way[i+1], Way[i]))
                    graph.InterfaceMatrix.Array[Way[i+1]][Way[i]] = 1
                    graph.InterfaceMatrix.Array[Way[i]][Way[i+1]] = 0
                i = i + 2
            i = 0
            while i < len(Way):
                P.append((Way[i], Way[i+1]))
                graph.InterfaceMatrix.Array[Way[i + 1]][Way[i]] = 1
                graph.InterfaceMatrix.Array[Way[i]][Way[i + 1]] = 0
                i = i + 2
            Xp.append(Way[0])
            Yp.append(Way[len(Way) - 1])
            tmpV1 = [x for x in graph.V1 if Xp.count(x) == 0]
            tmpV2 = [y for y in graph.V2 if Yp.count(y) == 0]
            if len(tmpV1) == len(tmpV2) and len(tmpV1) == 0:
                return P
            else:
                return self.__getPerfectMatchMinimumWeightAlgorithm(matrix, graph, Xp, Yp, P)
        else:
            X = []
            Y = []
            for x in tmpV1:
                ArrayMark = graph.searchWidth(x + 1)
                listArrayMark = [x-1 for x in ArrayMark.keys()]
                for top in listArrayMark:
                    if graph.V1.count(top) == 1:
                        if X.count(top) == 0:
                            X.append(top)
                    else:
                        if Y.count(top) == 0:
                            Y.append(top)
            m = None
            tmpV = [x for x in graph.V2 if Y.count(x) == 0]
            for x in X:
                for y in tmpV:
                    if matrix.Array[x][y - matrix.line] != '$':
                        if m is None:
                            m = matrix.Array[x][y - matrix.line]
                        elif m > matrix.Array[x][y - matrix.line]:
                            m = matrix.Array[x][y - matrix.line]
            sourceMatrix = matrix.copyMatrix()
            for x in X:
                for j in range(0, matrix.column):
                    if matrix.Array[x][j] != '$':
                        matrix.Array[x][j] = matrix.Array[x][j] - m
            for y in Y:
                j = y - matrix.line
                for i in range(0, matrix.line):
                    if matrix.Array[i][j] != '$':
                        matrix.Array[i][j] = matrix.Array[i][j] + m
            for x in X:
                for y in tmpV:
                    if matrix.Array[x][y - matrix.line] == 0:
                        graph.InterfaceMatrix.Array[x][y] = 1
            tmpX = [x for x in graph.V1 if X.count(x) == 0]
            for x in tmpX:
                for y in Y:
                    if matrix.Array[x][y - matrix.line] > sourceMatrix.Array[x][y - matrix.line]:
                        graph.InterfaceMatrix.Array[x][y] = 0
            return self.__getPerfectMatchMinimumWeightAlgorithm(matrix, graph, Xp, Yp, P)