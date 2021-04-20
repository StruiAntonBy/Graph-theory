def s_posled(matrix,n):
    i=0
    posled=[]
    x=0
    while i<n:
        j=0
        while j<n:
            if matrix[(i,j)]==1:
                x=x+1
            j=j+1
        posled.append(x)
        x=0
        i=i+1
    return posled

def getMatrix(list_top_graph,list_rib_graf):
    n=len(list_top_graph)
    matrix={}
    i=0
    while i<n:
        j=0
        while j<n:
            if list_rib_graf.count((i+1,j+1))==1:
                matrix[(i,j)]=1
            j=j+1
        i=i+1
    i=0
    while i<n:
        j=0
        while j<n:
            try:
                if matrix[(i,j)]!=1:
                    matrix[(i,j)]=0
            except KeyError:
                matrix[(i,j)]=0
            j=j+1
        i=i+1
    return matrix
