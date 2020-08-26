def find_target(input_matrix,target):
    #write your code here
    m=len(input_matrix)
    n=len(input_matrix[0])
    i=0
    j=n-1
    res=False
    while(i<m and j>=0):
        if input_matrix[i][j]==target:
            res=True
        if input_matrix[i][j]>target:
            j=j-1
        else:
            i=i+1
            
   
    return res
    
if __name__ == "__main__":
  input_matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
  ]
  target = 3
  print(find_target(input_matrix,target))




