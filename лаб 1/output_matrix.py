def print_line(matrix,i,n):
    j=0
    while j<n+1:
        print(matrix[(i,j)],end=' ')
        j=j+1

def print_matrix(matrix,n):
    i=0
    while i<n+1:
        print_line(matrix,i,n)
        print()
        i=i+1
