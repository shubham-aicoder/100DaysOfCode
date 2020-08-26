def find(n,r,res="",curr='9'):
    if n==0:
        r.append(res)
        return
    ch = ord(curr)
    while ch >= ord('0'):
        find(n - 1,r, chr(ch) + res, chr(ch - 1))
        ch=ch-1

    
    return sorted(r)



def strictly_increasing(input_number):
    r=[]
    #write your code here
    #return all possible outputs in a list
    n=input_number
    if n==1:
        for i in range(1,10):
            s=""
            s+=str(0)+str(i)
            r.append(s)
        return r
    else:
        return find(n,r)
        
                

    
if __name__ == "__main__":
  input_number = 2
  print(strictly_increasing(input_number))




