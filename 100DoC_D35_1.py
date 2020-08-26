# Function to find all N-digit strictly increasing
# numbers in Top-down manner
def strictlyInc(n,r,res="", curr='9'):
    # If the String becomes N-digit, print it
    if n == 0:
        r.append(res)
        return

    ch = ord(curr)
    while ch >= ord('0'):
        strictlyInc(n - 1,r, chr(ch) + res, chr(ch - 1))
        ch=ch-1

    
    return sorted(r)


if __name__ == '__main__':
    n = 2
    r=[]
    print(strictlyInc(n,r))
