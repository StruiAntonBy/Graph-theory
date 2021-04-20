def dataFile(FileName):
    f=open(FileName,'r')
    array=[x for x in f]
    f.close()
    n=len(array)
    matrix={}
    for i in range(0,n):
        matrix=fillMatrix(parseString(array[i]),matrix,i)
    return (matrix,n)

def parseString(S):
    list_elem=[]
    buffer=0
    for x in S:
        if x==' ' or x=='\n': 
            list_elem.append(int(buffer))
        else:
            buffer=x
    list_elem.append(int(buffer))
    return list_elem

def fillMatrix(list_elem,matrix,count):
    j=0
    while j<len(list_elem):
        matrix[(count,j)]=list_elem[j]
        j=j+1
    return matrix
