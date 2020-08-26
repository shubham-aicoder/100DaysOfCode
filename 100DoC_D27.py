def return_vertically(input_string):
    #write your code here
    
    l=input_string.split(" ")
    _max=len(l[0])
    for i in range(1,len(l)):
        if len(l[i])>_max:
            _max=len(l[i])
    j=0
    l1=[]
    while(j<=_max-1):
        l2=[]
        for i in l:
            try:
                l2+=i[j]
            except:
                l2+=' '
        l1.append(("".join(l2)).rstrip())
        j+=1
    return l1
if __name__ == "__main__":
  input_string = "HOW ARE YOU"
  print(return_vertically(input_string))




