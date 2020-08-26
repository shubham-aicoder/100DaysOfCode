def smallestDifference(arrayOne, arrayTwo):
  # Write your code here
  n=len(arrayOne)
  m=len(arrayTwo)
  arrayOne.sort()
  arrayTwo.sort()
  one=0
  two=0
  diff=9**9
  while(one<n and two<m):
      if abs(arrayOne[one]-arrayTwo[two])<diff:
          res_one=one
          res_two=two
          diff=abs(arrayOne[one]-arrayTwo[two])
      if arrayOne[one]<arrayTwo[two]:
          one=one+1
      else:
          two=two+1
  l=[arrayOne[res_one],arrayTwo[res_two]]
  return l
          
           
if __name__ == "__main__":
  arrayOne = [-1, 5, 10, 20, 28, 3]
  arrayTwo = [26, 134, 135, 15, 17]
  print(smallestDifference(arrayOne, arrayTwo))
