def sub(s,res,i=-1,curr_s=''):
    if i==len(s):
        return
    if len(curr_s)>0:
        res.append(curr_s)
    for k in range(i + 1, len(s)): 
        curr_s += s[k]
        sub(s,res,k,curr_s)

        curr_s = curr_s[:len(curr_s) - 1]
    
def power_set(input_string):
    #write your code here
    #return all possible outputs in a list
    #res = ["a","ab","abc","ac","b","bc","c"]
    input_string = ''.join(sorted(input_string))
    res=[]
    sub(input_string,res)           
    return sorted(list(set(res)))
if __name__ == "__main__":
  input_string = "banana"
  print(power_set(input_string))




    
    
