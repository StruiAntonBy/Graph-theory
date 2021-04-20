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

def distance_top(Arraytop):
    return max(Arraytop.values())

def radius(ListDistance_top):
    return min(ListDistance_top)

def diameter(ListDistance_top):
    return max(ListDistance_top)

def center_graf(ListDistance_top):
    list_center_graf=[x+1 for x in range(0,len(ListDistance_top)) if ListDistance_top[x]==radius(ListDistance_top)]
    return list_center_graf

def peripheral_center_graf(ListDistance_top):
    list_peripheral_center_graf=[x+1 for x in range(0,len(ListDistance_top)) if ListDistance_top[x]==diameter(ListDistance_top)]
    return list_peripheral_center_graf

def short_path(v1,v2,matrix,n):
    list_short_path=[]
    list_short_path.append(v2)
    arrayMark=search_width(v1-1,matrix,n)
    list_short_path=short_path_algorihm(v2-1,arrayMark[v2-1],arrayMark,matrix,list_short_path)
    list_short_path.append(v1)
    list_short_path.reverse()
    return list_short_path
    
def short_path_algorihm(start,mark,arrayMark,matrix,list_short_path):
    if mark==1:
        return list_short_path
    else:
        List_key_mark=return_key_in_dict(mark-1,arrayMark)
        i=0
        while i<len(List_key_mark):
            if matrix[(start,List_key_mark[i])]==1:
                list_short_path.append(List_key_mark[i]+1)
                break
            i=i+1
        return short_path_algorihm(List_key_mark[i],mark-1,arrayMark,matrix,list_short_path)
            
def return_key_in_dict(values,Dict):
    List_key=[]
    for x in Dict.keys():
        if Dict[x]==values:
            List_key.append(x)
    return List_key
            
    
