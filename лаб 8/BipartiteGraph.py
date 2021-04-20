from Graph import Graph
import copy


class BipartiteGraph(Graph):   # Двудольный граф

    def __init__(self, matrix, V1=None, V2=None):
        super().__init__(matrix)
        if V1 is None and V2 is None:
            self.V1 = []
            self.V2 = []
            self.__bipartite()
        else:
            self.V1 = V1
            self.V2 = V2

    def __bipartite(self):
        ArrayMark = self.searchWidth(1)
        for x in ArrayMark.keys():
            if ArrayMark[x] % 2 == 0:
                self.V2.append(x - 1)
            else:
                self.V1.append(x - 1)

    def getLargestMatch(self):   # Наибольшее паросочетание
        Xp = []
        Yp = []
        P = []
        self.V1.sort()
        self.V2.sort()
        for x in self.V1:
            for y in self.V2:
                if len(Xp) == 2:
                    break
                elif self.InterfaceMatrix.Array[x][y] == 1 and Xp.count(x) == 0 and Yp.count(y) == 0:
                    P.append((x, y))
                    Xp.append(x)
                    Yp.append(y)
        P = self.__LargestMatchAlgorithm(P, Xp, Yp, None)
        P = [(x[0]+1, x[1]+1) for x in P]
        return P

    def __LargestMatchAlgorithm(self, P, Xp, Yp, graph):
        matrix = None
        if graph is None:
            matrix = copy.deepcopy(self.InterfaceMatrix)
            for top1 in self.V1:
                for top2 in self.V2:
                    if self.InterfaceMatrix.Array[top1][top2] == 1:
                        matrix.Array[top2][top1] = 0
        else:
            matrix = copy.deepcopy(graph.InterfaceMatrix)
            for top1 in self.V1:
                for top2 in self.V2:
                    if graph.InterfaceMatrix.Array[top1][top2] == 1:
                        matrix.Array[top2][top1] = 0
        matrix.Array[P[0][1]][P[0][0]] = matrix.Array[P[1][1]][P[1][0]] = 1
        matrix.Array[P[0][0]][P[0][1]] = matrix.Array[P[1][0]][P[1][1]] = 0
        graph = Graph(matrix)
        tmpV1 = [x for x in self.V1 if Xp.count(x) == 0]
        tmpV2 = [x for x in self.V2 if Yp.count(x) == 0]
        for x in tmpV1:
            for y in tmpV2:
                Way = graph.getWay(x + 1, y + 1)
                if Way is not None:
                    Way = [x - 1 for x in Way]
                    i = 0
                    while i < len(Way):
                        P.append((Way[i], Way[i + 1]))
                        if Xp.count(Way[i]) == 0:
                            Xp.append(Way[i])
                        if Yp.count(Way[i + 1]) == 0:
                            Yp.append(Way[i + 1])
                        i = i + 2
                    Pdel = []
                    i = len(Way) - 2
                    while i > 0:
                        Pdel.append((Way[i], Way[i - 1]))
                        i = i - 2
                    for p in Pdel:
                        if P.count(p) == 1:
                            P.remove(p)
                    return self.__LargestMatchAlgorithm(P, Xp, Yp, graph)
        tmp = []
        tmpP = []
        for x in P:
            if tmp.count(x[0]) == 0 and tmp.count(x[1]) == 0:
                tmp.append(x[0])
                tmp.append(x[1])
                tmpP.append(x)
        P = tmpP
        return P