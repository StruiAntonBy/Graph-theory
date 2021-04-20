def detect_cycle(posled_graph):
    n=len(posled_graph)
    i=0
    x=0
    list_x=[]
    while i<n:
        if posled_graph[i]%2!=0:
            x=x+1
            list_x.append(i+1)
        i=i+1
    if x==2:
        return (False,list_x)
    elif x==0:
        return (True,None)
    else:
        return (None,None)

def find(v,list_rib_graf):
    i=0
    n=len(list_rib_graf)
    while i<n:
        buf=list_rib_graf[i]
        if buf[0]==v:
            return True
        i=i+1
    return False

def cicle(list_top_graph,list_rib_graf):
    Path=[]
    v=list_top_graph[0]
    while len(list_rib_graf)!=0:
        if len(Path)!=0:
            i=0
            while i<len(Path):
                buf=Path[0]
                if find(buf[0],list_rib_graf):
                    v=buf[0]
                    break
                i=i+1
        c=v
        P=[]
        u=0
        while u!=c:
            i=0
            while i<len(list_rib_graf):
                buf=list_rib_graf[i]
                if buf[0]==v:
                    u=buf[1]
                    break
                i=i+1
            P.append((v,u))
            list_rib_graf.remove((v,u))
            list_rib_graf.remove((u,v))
            v=u
        if len(Path)!=0:
            buf=P[0]
            i=0
            while i<len(Path):
                if buf[0]==Path[i][0]:
                    j=0
                    list_start=[]
                    i1=0
                    while i1<i:
                        list_start.append(Path[i1])
                        i1+1
                    j=0
                    while j<len(P):
                        list_start.append(P[j])
                        j=j+1
                    j=i1
                    while j<len(Path):
                        list_start.append(Path[j])
                        j=j+1
                    Path=list_start
                    break
                i=i+1
        else:
            Path=P
    return Path

def list_append(listData,listArg):
    i=0
    n=len(listArg)
    while i<n:
        listData.append(listArg[i])
        i=i+1
    return listData

def find_fictional_rib(rib,Path):
    n=len(Path)
    i=0
    while i<n:
        if Path[i]==rib:
            return i
        i=i+1
    return None

def getchain(i,Path):
    n=len(Path)
    chain=[]
    j=i+1
    while j<n:
        chain.append(Path[j])
        j=j+1
    j=0
    while j<i:
        chain.append(Path[j])
        j=j+1
    return chain
        

def algorithm(list_top_graph,list_rib_graf,posled_graph):
    (boolDetect,list_namber)=detect_cycle(posled_graph)
    if boolDetect==True:
        print("Существует Эйлеровый цикл!")
        print(cicle(list_top_graph,list_rib_graf))
    elif boolDetect==False:
        print("Существует Эйлерова цепь!")
        list_rib_graf.append((list_namber[0],list_namber[1]))
        list_rib_graf.append((list_namber[1],list_namber[0]))
        Path=cicle(list_top_graph,list_rib_graf)
        i=find_fictional_rib((list_namber[0],list_namber[1]),Path)
        if i!=None:
            print(getchain(i,Path))
        else:
            i=find_fictional_rib((list_namber[1],list_namber[0]),Path)
            print(getchain(i,Path))
    else:
        print("Граф не обладает Эйлеровым циклом!")
        print("Граф не обладает Эйлеровой цепью!")
        
