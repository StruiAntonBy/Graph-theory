import input_data_file as in_data
import numpy

def data():
    n=0
    m=0
    matrix={}
    (matrix,n,m)=in_data.input_data("data.txt");
    array=[]
    i=0
    n=n+1
    while i<n:
        l=[matrix[(i,x)] for x in range(0,n)]
        array.append(l)
        i=i+1
    matrix=numpy.array(array)
    return (matrix,n)
