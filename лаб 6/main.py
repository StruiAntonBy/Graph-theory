import inputData as In
import script as scr

(matrix,n)=In.dataFile("data.txt")
print("Матрица смежности:")
scr.ShowMatrix(matrix,n)
res=scr.determinegraf(matrix,n)
if res==True:
    print("Заданный граф - дерево")
    PruferCode=scr.getPruferCode(matrix,n)
    for x in range(0,len(PruferCode)):
        PruferCode[x]=PruferCode[x]+1
    print("1.Код Прюфера:",PruferCode)
    PruferCode=scr.inputPruferCode()
    print("Код Прюфера:",PruferCode)
    for x in range(0,len(PruferCode)):
        PruferCode[x]=PruferCode[x]-1
    (matrix,n)=scr.getMatrix(PruferCode)
    print("2.Матрица смежности:")
    scr.ShowMatrix(matrix,n)
    (matrix,n)=In.dataFile("data.txt")
    print("Матрица смежности:")
    scr.ShowMatrix(matrix,n)
    root=int(input("Введите корень дерева:"))-1
    BinaryCode=scr.getBinaryCode(root,matrix,n)
    StringBinaryCode=''
    for x in BinaryCode:
        StringBinaryCode=StringBinaryCode+str(x)
    print("3.Бинарный код:",StringBinaryCode)
    input('Нажмите Enter для выхода\n')
elif res==None:
    print("Заданный граф несвязный")
    input('Нажмите Enter для выхода\n')
else:
    print("Заданный граф - не дерево")
    input('Нажмите Enter для выхода\n')
    
