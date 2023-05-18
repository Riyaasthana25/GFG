def printFirstNegativeInteger( a,n,k):
    # code here
    ws=0
    we=k
    res=[]
    while we<=n:
        b=a[ws:we]
        c=0
        for i in b:
            if i < 0:
                res.append(i)
                c=1 
                break
        if c==0:
            res.append(0)
        ws+=1
        we+=1
    return res
