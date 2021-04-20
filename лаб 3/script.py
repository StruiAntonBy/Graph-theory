import numpy

def pow_matrix(matrix,n):
    i=1
    resultMatrix=matrix
    while i<n:
        resultMatrix=numpy.dot(resultMatrix,matrix)
        i=i+1    
    return resultMatrix

def sign(matrix,n):
    matrix_access=numpy.eye(n,None,0,'int')
    i=1
    while i<n:
        matrix_access=matrix_access+pow_matrix(matrix,i)
        i=i+1
    i=0
    while i<n:
        j=0
        while j<n:
            if matrix_access[i,j]>0:
                matrix_access[i,j]=1
            elif matrix_access[i,j]<0:
                matrix_access[i,j]=-1
            j=j+1
        i=i+1
    return matrix_access

def matrix_power_connectiv(matrix,n):
    matrix_access=sign(matrix,n)
    return matrix_access*matrix_access.T

def component_power_connectiv(matrix,n):
    matrix_S=matrix_power_connectiv(matrix,n)
    V=[x+1 for x in range(0,n)]
    p=0
    while len(matrix_S)!=0:
        p=p+1
        i=0
        K=[]
        while i<len(matrix_S):
            if matrix_S[0,i]==1:
                K.append(V[i])
            i=i+1
        matrix_G=numpy.zeros((len(K),len(K)),int)
        i=0
        while i<len(K):
            j=0
            while j<len(K):
                if matrix[K[i]-1,K[j]-1]==1:
                    matrix_G[i,j]=1
                j=j+1
            i=i+1
        print("V"+str(p),end="=")
        print(K)
        print(matrix_G)
        matrix_s=[]
        i=0
        while i<len(V):
            j=0
            l=[]
            while j<len(V):
                if K.count(n-len(matrix_S)+i+1)==0 and K.count(n-len(matrix_S)+j+1)==0:
                   l.append(matrix_S[i,j])  
                j=j+1
            if K.count(n-len(matrix_S)+i+1)==0:
                matrix_s.append(l)
            i=i+1
        matrix_S=numpy.array(matrix_s)
        i=0
        while i<len(K):
            V.remove(K[i])
            i=i+1
        
        
    
