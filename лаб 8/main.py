from Matrix import Matrix
from WeightedBipartiteGraph import WeightedBipartiteGraph

matrix = Matrix()
matrix.setMatrixFile('data.txt')
graph = WeightedBipartiteGraph(matrix)
print("Матрица весов:")
graph.print_WeightMatrix()
if graph.PerfectMatchMinimumWeight():
    print("Существует совершенное паросочетание минимального веса.")
    (P, Sum) = graph.getPerfectMatchMinimumWeight()
    print("P =", P, " Sum =", Sum)
else:
    print("Не существует совершенного паросочетания минимального веса.")
input('Нажмите Enter для выхода\n')
