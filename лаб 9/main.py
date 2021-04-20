from Matrix import Matrix
from Graph import Graph

matrix = Matrix()
matrix.setMatrixFile('data.txt')
graph = Graph(matrix)
result = graph.GreedyColorizationAlgorithm()
i = 0
print("Жадный алгоритм раскрашивания:")
for x in result:
    i = i + 1
    print(str(i) + ".", "C =", x[0], "f(v) =", x[1], "∀v∈C")
result = graph.AlgorithmSequentialColoring()
print("Алгоритм последовательного раскрашивания:")
for x in result.keys():
    print("f(v"+str(x)+") =", result[x])
input('Нажмите Enter для выхода\n')