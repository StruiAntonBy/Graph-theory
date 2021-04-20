import itertools

def find_ribs(matrix):
    n=0
    for val in matrix.values():
        if val==1:
            n=n+1
    return n/2

def s_posled(matrix,n):
    i=0
    posled=[]
    x=0
    while i<n+1:
        j=0
        while j<n+1:
            if matrix[(i,j)]==1:
                x=x+1
            j=j+1
        posled.append(x)
        x=0
        i=i+1
    return posled

def match(P,matrix1,matrix2,n):
    i=0
    sootvetstvie={}
    while i<n+1:
        j=0
        while j<n+1:
            if matrix1[(i,j)]!=matrix2[(P[i],P[j])]:
                return False
            j=j+1
            sootvetstvie[i+1]=P[i]+1
        i=i+1
    print(sootvetstvie)
    return True

def algoritm(matrix1,matrix2,n1,n2):
    P=[x for x in range(0,n1+1)]
    P=list(itertools.permutations(P,n1+1))
    i=0
    while i<len(P):
        x=P[i]
        if match(x,matrix1,matrix2,n1)==True:
            return True
        i=i+1
    return False
    
def isomorphic(matrix1,matrix2,n1,n2):
    if len(matrix1)==len(matrix2):
        if find_ribs(matrix1)==find_ribs(matrix2):
            if s_posled(matrix1,n1)==s_posled(matrix2,n2):
                return True
            else:
                if algoritm(matrix1,matrix2,n1,n2)==True:
                    return True
                else:
                    return False
        else:
            return False
    else:
        return False
