def ShowMatrix(matrix,n):
    for i in range(0,n):
        for j in range(0,n):
            print(matrix[(i,j)],end=' ')
        print()

def getMatrixS(matrix,n):
    matrixS={}
    for i in range(0,n):
        for j in range(0,n):
            if matrix[(i,j)]=='%' or matrix[(i,j)]=='$':
                matrixS[(i,j)]=0
            else:
                matrixS[(i,j)]=1
    return matrixS

def determinegraf(matrixS,n):
    if search_width(0,matrixS,n)==None:
        return None
    elif n-getRibs(matrixS,n)!=1:
        return False
    else:
        return True

def getRibs(matrixS,n):
    Ribs=0
    for i in range(0,n-1):
        j=i+1
        for x in range(j,n):
            if matrixS[(i,x)]==1:
                Ribs=Ribs+1
    return Ribs

def getArray(matrix,n):
    Array=[]
    for i in range(0,n):
        line=[]
        for j in range(0,n):
            line.append(matrix[(i,j)])
        Array.append(line)
    return Array

def search_cycle(tops):
    for x in tops:
        if tops.count(x)==2:
            return True
    return False

#####################################################################################################

def algorithmKruskal(matrix, n):
    listTops = []
    Ribs = {}
    AllRibs = getAllRibs(matrix, n)
    while len(AllRibs) != 0:
        MinRib = getminrib(AllRibs)
        Ribs[MinRib] = matrix[MinRib]
        del AllRibs[(MinRib[1], MinRib[0])]
        del AllRibs[MinRib]
        listRibs = [x for x in Ribs.keys()]
        N = len(listRibs)
        i = 0
        while i<N:
            rib = listRibs[i]
            listRibs.append((rib[1], rib[0]))
            i=i+1
        Tops = listTops
        for x in MinRib:
                if Tops.count(x) == 0:
                    Tops.append(x)
        if cycle(listRibs, Tops)==True:
            del Ribs[MinRib]
        else:
            for x in MinRib:
                if listTops.count(x) == 0:
                    listTops.append(x)
    return (listTops, Ribs)


def getAllRibs(matrix, n):
    Ribs = {}
    for i in range(0, n):
        for j in range(0, n):
            if matrix[(i, j)] != '%' and matrix[(i, j)] != '$':
                Ribs[(i, j)] = matrix[(i, j)]
    return Ribs

def getminrib(Ribs):
    Min = None
    for x in Ribs.keys():
        if Min is None:
            Min = x
        else:
            if Ribs[Min] > Ribs[x]:
                Min = x
    return Min

def cycle(listRibs, listTops):
    if len(listRibs) == 0:
        return False
    else:
        TopVisited=[listTops[0]]
        i=0
        Ribs=listRibs
        while i<len(TopVisited):
            j=0
            while j<len(Ribs):
                if Ribs[j][0]==TopVisited[i] and TopVisited.count(Ribs[j][1])==1:
                    return True
                elif Ribs[j][0]==TopVisited[i]:
                    TopVisited.append(Ribs[j][1])
                    del1=Ribs[j]
                    del2=(Ribs[j][1],Ribs[j][0])
                    Ribs.remove(del2)
                    Ribs.remove(del1)
                    j=0
                else:
                    j=j+1
            i=i+1
        return False
                
##################################################################################################

def getindependedTop(rib,list_tops):
    x=rib[0]
    y=rib[1]
    if list_tops.count(x)==1:
        return y
    elif list_tops.count(y)==1:
        return x

def getMinRibs(Ribs,matrix):
    Min=0
    for x in Ribs:
        if Min==0:
            Min=x
        else:
            if matrix[x]<matrix[Min]:
                Min=x
    return Min

def getArrayAllribs(matrixS,n):
    Ribs=[]
    for i in range(0,n):
        for j in range(0,n):
            if matrixS[(i,j)]==1:
                Ribs.append((i,j))
    return Ribs

def getindependedRibs(ribs,list_tops):
    list_ribs=[]
    for x in ribs:
        if list_tops.count(x[0])==1 or list_tops.count(x[1])==1:
            list_ribs.append(x)
    return list_ribs
    

def algorithmPrima(matrix,n):
    Array=getArray(matrix,n)
    (Min,stroka,stolbec)=getMinArray(Array,list(x for x in range(0,n)),list())
    list_good=[stroka,stolbec]
    list_ribs={(stroka,stolbec):Array[stroka][stolbec]}
    while len(list_good)!=n:
        (Min,stroka,stolbec)=getMinArray(Array,list_good,list_good)
        list_good.append(stolbec)
        list_ribs[(stroka,stolbec)]=Array[stroka][stolbec]
    return (list_good,list_ribs)

def beautiful_output(Text,tops,ribs):
    print(Text,end=":")
    for x in range(0,len(tops)):
        tops[x]=tops[x]+1
    print("T(G)=(",tops,end=",")
    Ribs=list(ribs.keys())
    Sum=sumRibsTree(ribs)
    ribs=[]
    for x in Ribs:
        ribs.append((x[0]+1,x[1]+1))
    print(ribs,end=") sum=")
    print(Sum)

def sumRibsTree(list_ribs):
    Sum=0
    for x in list_ribs.values():
        Sum=Sum+x
    return Sum
            
def getMinArray(Array,list_good,list_ignore):
    Min=None
    index=0
    Line=0
    for i in list_good:
        if Min==None:
            (Min,index)=getMinLine(Array[i],list_ignore)
            Line=i
        else:
            (x,j)=getMinLine(Array[i],list_ignore)
            if x==None:
                continue
            elif Min>x:
                Min=x
                index=j
                Line=i
    return (Min,Line,index)
    
def getMinLine(Line,list_ignore):
    Min=None
    index=0
    j=0
    while j<len(Line):
        if list_ignore.count(j)==1:
            j=j+1
            continue
        elif Line[j]=='%' or Line[j]=='$':
            j=j+1
            continue
        else:
            if Min==None:
                Min=Line[j]
                index=j
            elif Min>Line[j]:
                Min=Line[j]
                index=j
            j=j+1    
    return (Min,index)
        
def search_width(top,matrix,n):
    arrayMark={}
    list_top_metka=[]
    list_top_metka.append(top)
    i=0
    metka=1
    while len(list_top_metka)!=n and i<n:
        try:
            top=list_top_metka[i]
            if arrayMark.get(top)==None:
                (arrayMark,list_top_metka)=search_width_algorithm(arrayMark,list_top_metka,top,matrix,n,metka)
            else:
                (arrayMark,list_top_metka)=search_width_algorithm(arrayMark,list_top_metka,top,matrix,n,arrayMark.get(top)+1)
            i=i+1
        except IndexError:
            return None 
    return arrayMark

def search_width_algorithm(arrayMark,list_top_metka,top,matrix,n,metka):
    j=0
    while j<n:
        if matrix[(top,j)]==1 and list_top_metka.count(j)==0:
            list_top_metka.append(j)
            arrayMark[j]=metka
        j=j+1
    return (arrayMark,list_top_metka)
