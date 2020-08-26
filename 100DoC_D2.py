import itertools
def threeNumberSum(array,targetSum):
    """
    """
    j=0
    l=[]
    res=[]
    d=dict.fromkeys(array,0)
    for i in d:
        d[i]=j
        j+=1
    for i in range(len(array)):
        for k in range(i+1,len(array)):
            l.append((array[i],array[k]))
    for i in range(len(l)):
        value=targetSum-sum(l[i])
        if value in d.keys() and (value not in l[i]):
            res.append(l[i]+(value,))
    for i in range(len(res)):
        res[i]=sorted(res[i])
    res.sort()
    res=list(res for res,_ in itertools.groupby(res))

    
        
        

    if len(res)!=0:
        return res
    else:
        return []        
            
        
    
            
    





if __name__=='__main__':
    array=[12,2,1,3,-6,5,-8,6]
    targetSum=0
    print(threeNumberSum(array,targetSum))
