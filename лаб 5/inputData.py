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
    buffer=''
    for x in S:
        if x=='%' or x=='$':
            list_elem.append(x)
        elif x==' ' or x=='\n':
            if buffer!='': 
                list_elem.append(int(buffer))
                buffer=''
            else:
                buffer=''
        else:
            buffer=buffer+x
    return list_elem

def fillMatrix(list_elem,matrix,count):
    j=0
    while j<len(list_elem):
        matrix[(count,j)]=list_elem[j]
        j=j+1
    return matrix
