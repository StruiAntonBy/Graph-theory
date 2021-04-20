import input as in_
import matrix_methods
import script as scr

n=int(input('Введите количество вершин:'))
m=int(input('Введите количество ребер:'))
(list_top_graph,list_rib_graf)=in_.data(n,m)
list_top_graph=[x for x in range(1,8)]
#list_rib_graf=[(1,2),(2,1),(2,3),(3,2),(3,4),(4,3),(4,7),(4,7),(7,4),(7,4),(6,7),(7,6),(6,1),(1,6),(1,5),(5,1),(2,6),(6,2),(2,5),(5,2),(6,5),(5,6),(3,5),(5,3),(5,7),(7,5),(5,4),(4,5)]
posled_graph=matrix_methods.s_posled(matrix_methods.getMatrix(list_top_graph,list_rib_graf),len(list_top_graph))
scr.algorithm(list_top_graph,list_rib_graf,posled_graph)
input('Нажмите Enter для выхода\n')
