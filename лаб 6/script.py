def PowPosled(matrix,n,list_ignore):
    posled={}
    Pow=0
    list_tops=list(range(0,n))
    for i in range(0,len(list_ignore)):
        list_tops.remove(list_ignore[i])
    for i in list_tops:
        for j in range(0,n):
            if matrix[(i,j)]==1:
                Pow=Pow+1
        posled[i]=Pow
        Pow=0
    return posled

def getMinPowPosled(powposled):
    for x in powposled.keys():
        if powposled[x]==1:
            return x

def getPruferCode(matrix,n):
    PruferCode=[]
    list_ignore=[]
    N=n
    while N!=2:
        powposled=PowPosled(matrix,n,list_ignore)
        i=getMinPowPosled(powposled)
        list_ignore.append(i)
        independed=0
        for j in range(0,n):
            if matrix[(i,j)]==1:
                independed=j
                break
        for j in range(0,n):
            del matrix[(i,j)]
        matrix[(independed,i)]=0
        PruferCode.append(independed)
        N=N-1
    return PruferCode

def ShowMatrix(matrix,n):
    for i in range(0,n):
        for j in range(0,n):
            print(matrix[(i,j)],end=' ')
        print()

def determinegraf(matrix,n):
    if search_width(0,matrix,n)==None:
        return None
    elif n-getRibs(matrix,n)!=1:
        return False
    else:
        return True

def getRibs(matrix,n):
    Ribs=0
    for i in range(0,n-1):
        j=i+1
        for x in range(j,n):
            if matrix[(i,x)]==1:
                Ribs=Ribs+1
    return Ribs

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

def inputPruferCode():
    S=input("Введите код Прюфера:")
    buf=''
    PruferCode=[]
    for x in S:
        if x==' ':
          PruferCode.append(int(buf))
          buf=''
        buf=buf+x
    PruferCode.append(int(buf))
    return PruferCode

def getMatrix(PruferCode):
    n=len(PruferCode)+2
    tops=list(x for x in range(0,n))
    matrix={}
    for i in range(0,n):
        for j in range(0,n):
            matrix[(i,j)]=0
    while len(PruferCode)!=0:
        Min=getMinTop(tops,PruferCode)
        i=PruferCode.pop(0)
        tops.remove(Min)
        matrix[i,Min]=matrix[Min,i]=1
    i=tops.pop(0)
    j=tops.pop(0)
    matrix[i,j]=matrix[j,i]=1
    return (matrix,n)
    
def getMinTop(tops,PruferCode):
    List=[x for x in tops if PruferCode.count(x)==0]
    return min(List)

def getBinaryCode(root,matrix,n):
    BinaryCode=[]
    prev=-1
    List_visited={root:prev}
    while len(List_visited)!=n:
        j=0
        while j<n:
            if matrix[(root,j)]==1 and list(List_visited.keys()).count(j)==0:
                List_visited[j]=root
                root=j
                BinaryCode.append(1)
                j=0
                continue
            j=j+1
        root=List_visited[root]
        BinaryCode.append(0)
    while root!=-1:
        root=List_visited[root]
        if root==-1:
            break
        BinaryCode.append(0)
    return BinaryCode
