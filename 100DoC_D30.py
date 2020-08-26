import collections
def sum_tree(input_matrix,sum_val):
    #write your code here
    dic=collections.defaultdict(int)
    stack=[]
    for i in range(len(input_matrix)):
        if input_matrix[i]!=None:
            stack.append((input_matrix[i],1))
    print(stack)
    count=0
    prev=0
    dic[0]=1
    while stack:
        node,meet=stack.pop(0)
        j=input_matrix.index(node)
        print(j)
        if meet==1:
            prev+=node
            if prev-sum_val in dic:
                count+=dic[prev-sum_val]
            dic[prev]+=1
            stack.append((node,meet+1))
            if input_matrix[2*j+1]:
                stack.append((input_matrix[2*j+1],1))
        elif meet==2:
            stack.append((node,meet+1))
            if input_matrix[2*j+2]:
                stack.append((input_matrix[2*j+2],1))

        else:
            dic[prev]-=1
            prev-=node
    return count

if __name__ == "__main__":
  input_matrix = [10,5,-3,3,2,None,11,3,-2,None,1]
  sum_val = 8
  print(sum_tree(input_matrix,sum_val))




