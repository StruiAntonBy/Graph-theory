import input_data_file as in_f
import scripts as scr

matrix={}
n=0
m=0
(matrix,n,m)=in_f.input_data('data.txt')
print("Задание 1:",scr.s_posled(matrix,n+1))
print("Задание 2:")
i=0
ListDistance_top=[]
if scr.search_width(0,matrix,n+1)==None:
    print("Несвязный граф")
    input('Нажмите Enter для выхода\n')
    exit(0)
while i<n+1:
    ListDistance_top.append(scr.distance_top(scr.search_width(i,matrix,n+1)))
    print("Удаленность вершины ",i+1,end=":")
    print(ListDistance_top[i])
    i=i+1
print("Радиус графа:",scr.radius(ListDistance_top))
print("Диаметр графа:",scr.diameter(ListDistance_top))
print("Центры графа:",scr.center_graf(ListDistance_top))
print("Периферийные центры графа:",scr.peripheral_center_graf(ListDistance_top))
print("Задание 3:")
v1=int(input("Введите 1 вершину графа:"))
v2=int(input("Введите 2 вершину графа:"))
print("Кратчайший маршрут:",scr.short_path(v1,v2,matrix,n+1))
input('Нажмите Enter для выхода\n')


        
    
               
                
        
