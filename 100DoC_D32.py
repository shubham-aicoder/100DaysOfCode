res=[]
def check_palindrome(s,low,high):
    while low<high:
        if s[low]!=s[high]:
            return False
        low+=1
        high-=1
    return True
def all_part(store_part,curr_part,start,n,s):
    if start>=n:
        x=curr_part.copy()
        store_part.append(x)
        return
    for i in range(start,n):
        if check_palindrome(s,start,i):
            curr_part.append(s[start:i+1])
            all_part(store_part,curr_part,i+1,n,s)
            curr_part.pop()

def recursive_palindrome(input_string):
    #write your code here
    #return all possible outputs in a list
    #res = ["n i t i n","n iti n","nitin"]
    n=len(input_string)
    store_part=[]
    curr_part=[]
    

    all_part(store_part,curr_part,0,n,input_string)

    for i in range(len(store_part)):
        st=''
        for j in range(len(store_part[i])):
            if j==len(store_part[i])-1:
                st=st+store_part[i][j]
            else:
                st=st+store_part[i][j]+" "
            #print(store_part[i][j],end=' ')
        res.append(st)
        #print("")
    return res
if __name__ == "__main__":
  input_string = "nitin"
  print(recursive_palindrome(input_string))




