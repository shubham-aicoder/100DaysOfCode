def ip_check(input_string):
    #write your code here
    #return all possible outputs in a list

    if int(input_string)>=0 and int(input_string)<=255 and not(len(input_string)>1 and input_string[0]=='0'):
        return True
    else:
        return False
def valid_ip(input_string):
    n=len(input_string)
    if n>12 or n<4:
        return []
    res=[]
    for i in range(n-3):
        for j in range(i+1,n-2):
            for k in range(j+1,n-1):
                if ip_check(input_string[:i+1]) and ip_check(input_string[i+1:j+1]) and ip_check(input_string[j+1:k+1]) and ip_check(input_string[k+1:]):
                    res.append(".".join([input_string[:i+1],input_string[i+1:j+1],input_string[j+1:k+1],input_string[k+1:]]))
    return res
if __name__ == "__main__":
  input_string = "101023"
  print(valid_ip(input_string))




