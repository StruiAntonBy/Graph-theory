def input_data(name_file):
    f=open(name_file,'r')
    matrix={}
    i=0
    j=0
    minus=''
    string=f.read()
    f.close()
    for x in string:
        x=minus+x
        if x==' ':
            j=j+1
            minus=''
        elif x=='\n':
            i=i+1
            j=0
            minus=''
        elif x=='-':
            minus='-'
            continue
        else:
            matrix[(i,j)]=int(x)
            minus=''
    return (matrix,i,j)


        
        

