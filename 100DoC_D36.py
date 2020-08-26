def find(chars,i,s,l,res):
    if i==0:
        res.append(s)
        return 
    for j in range(0,l):
        a=s+chars[j]
        find(chars,i-1,a,l,res)


def hack_it(chars,length):
    #write your code here
    #return all possible outputs in a list
    res=[]
    for i in range(1,length+1):
        find(chars,i,"",length,res)
        if i==length:
            return res
if __name__ == "__main__":
  chars = ['a',"b"] 
  print(hack_it(chars,len(chars)))




