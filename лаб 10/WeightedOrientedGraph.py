from OrientedGraph import OrientedGraph
from Matrix import Matrix

class WeightedOrientedGraph(OrientedGraph):   # Взвешенный ориентированный граф

    def __init__(self, WeightMatrix):
        self.WeightMatrix = WeightMatrix   # Матрица весов
        self.InterfaceMatrix = Matrix()   # Матрица смежности
        self.InterfaceMatrix.initializeMatrix(self.WeightMatrix.line, self.WeightMatrix.column)
        for line in range(0, self.WeightMatrix.line):
            for column in range(0, self.WeightMatrix.column):
                if self.WeightMatrix.Array[line][column] == '$' or self.WeightMatrix.Array[line][column] == 0:
                    self.InterfaceMatrix.Array[line][column] = 0
                else:
                    self.InterfaceMatrix.Array[line][column] = 1

    def searchShortestPath(self, Top):   # Поиска кратчайшего пути
        V = {x for x in range(0, self.WeightMatrix.line)}
        table = {x: [] for x in range(0, self.WeightMatrix.line)}
        U = {Top - 1}
        (d, p, leading, array) = (0, None, Top-1, dict())
        for x in V.difference(U):
            array[x] = self.WeightMatrix.Array[leading][x]
            table[x].append(self.WeightMatrix.Array[leading][x])
            table[x].append(leading)
        table[leading].append(d)
        table[leading].append(p)
        table[leading].append(array)
        while len(U) != len(V):
            leading = self.__minArray(array)
            U.add(leading)
            array = dict(array)
            array.pop(leading)
            d = table[leading][0]
            for x in array.keys():
                if self.incidentTops(leading+1, x+1):
                    if array[x] != '$':
                        if self.WeightMatrix.Array[leading][x] + d < array[x]:
                            array[x] = self.WeightMatrix.Array[leading][x] + d
                            table[x][0] = array[x]
                            table[x][1] = leading
                    else:
                        array[x] = self.WeightMatrix.Array[leading][x] + d
                        table[x][0] = array[x]
                        table[x][1] = leading
            table[leading].append(array)
        V.remove(Top - 1)
        result = []
        for x in V:
            tmp = table[x]
            L = [tmp[0], (Top, x+1)]
            way = [x]
            leading = tmp[1]
            while Top-1 != leading:
                way.append(leading)
                tmp = table[leading]
                leading = tmp[1]
            way.append(leading)
            way.reverse()
            way = [x+1 for x in way]
            L.append(way)
            result.append(L)
        return result

    def __minArray(self, array):
        minTop = None
        for key in array.keys():
            if array[key] != '$':
                if minTop is None:
                    minTop = key
                elif array[minTop] > array[key]:
                    minTop = key
        return minTop