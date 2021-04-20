import identification_graf as ident_graf

def return_v(find_x,i,j,n,matrix):
    while i<n+1:
        if matrix[(i,j)]==find_x:
            return i
        i=i+1

def filling_zero(matrix,i,n):
    j=0
    while j<n+1:
        try:
            if matrix[(i,j)]!=1:
                matrix_s[(i,j)]=0
            j=j+1
        except KeyError:
            matrix[(i,j)]=0
            j=j+1
    return matrix
        
def return_matrix_s(matrix,n,m):
    matrix_s={}
    graf=False
    if ident_graf.indefication(matrix)=='no oriented':
        graf=True
    i=0
    j=0
    while j<m+1:
        if graf==True:
            i1=return_v(1,i,j,n,matrix)
            i2=return_v(1,i1+1,j,n,matrix)
            matrix_s[(i1,i2)]=matrix_s[(i2,i1)]=1
            i=0
            j=j+1
        else:
            i1=return_v(-1,i,j,n,matrix)
            i2=return_v(1,i,j,n,matrix)
            matrix_s[(i1,i2)]=1
            i=0
            j=j+1
    while i<n+1:
        matrix_s=filling_zero(matrix_s,i,n)
        i=i+1
    return matrix_s


        
    
               
                
        
