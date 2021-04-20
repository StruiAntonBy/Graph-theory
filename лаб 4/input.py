def data(n,m):
    list_top_graph=[x for x in range(1,n+1)]
    list_rib_graf=[]
    for x in range(0,m):
        print('Ребро '+str(x+1))
        u=int(input('u='))
        v=int(input('v='))
        list_rib_graf.append((u,v))
        list_rib_graf.append((v,u))
    return (list_top_graph,list_rib_graf)
