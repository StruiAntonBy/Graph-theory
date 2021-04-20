import inputData as In
import script as scr

(matrix,n)=In.dataFile("data.txt")
print("Исходная матрица:")
scr.ShowMatrix(matrix,n)
print("Матрица смежности:")
matrixS=scr.getMatrixS(matrix,n)
scr.ShowMatrix(matrixS,n)
res=scr.determinegraf(matrixS,n)
if res==True:
    print("Заданный граф - дерево")
    input('Нажмите Enter для выхода\n')
    exit()
elif res==None:
    print("Заданный граф несвязный")
    input('Нажмите Enter для выхода\n')
    exit()
else:
    print("Заданный граф - не дерево")
    (tops,ribs)=scr.algorithmPrima(matrix,n)
    scr.beautiful_output("Алгоритм Прима",tops,ribs)
    (tops,ribs)=scr.algorithmKruskal(matrix,n)
    scr.beautiful_output("Алгоритм Краскала",tops,ribs)
    input('Нажмите Enter для выхода\n')
    
