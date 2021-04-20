from Matrix import Matrix
from WeightedOrientedGraph import WeightedOrientedGraph

matrix = Matrix()
matrix.setMatrixFile('data.txt')
graph = WeightedOrientedGraph(matrix)
top = int(input("Введите вершину:"))
result = graph.searchShortestPath(top)
for x in result:
    print("l", x[1], "=", x[0], " Path =", x[2])
input('Нажмите Enter для выхода\n')