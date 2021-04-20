from Matrix import Matrix
from Graph import Graph
from BipartiteGraph import BipartiteGraph

matrix = Matrix('data.txt')
graph = Graph(matrix)
print("Матрица смежности:")
graph.print_InterfaceMatrix()
if graph.bipartite():
    print("Заданный граф двудольный.")
    graph = BipartiteGraph(matrix)
    print("Наибольшее паросочетание:", graph.getLargestMatch())
else:
    print("Заданный граф не является двудольным.")
input('Нажмите Enter для выхода\n')
