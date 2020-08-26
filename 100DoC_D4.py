import itertools
def fourNumberSum(array, targetSum):
    # Write your code here.
    l=[]
    t=[]
    res=[]
    j=0
    for i in range(len(array)):
        for k in range(i+1,len(array)):
            l.append((array[i],array[k]))
            t.append(array[i]+array[k])
    d=dict.fromkeys(t,0)
    for i in d:
        d[i]=j
        j+=1
    for i in range(len(l)):
        value=targetSum-sum(l[i])
        if value in d.keys() and (value not in l[i]):
            if set(l[i]).intersection(set(l[t.index(value)]))==set():
                res.append(l[i]+l[t.index(value)])
    for i in range(len(res)):
        res[i]=sorted(res[i])
    res.sort()
    res=list(res for res,_ in itertools.groupby(res))
    if len(res)!=0:
        return res
    else:
        return []
if __name__ == "__main__":
  array = [7,6,4,-1,1,2]
  targetSum = 16
  output = fourNumberSum(array, targetSum)
  print(output)
  
