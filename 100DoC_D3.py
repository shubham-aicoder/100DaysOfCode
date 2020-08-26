def smallestDifference(arrayOne, arrayTwo):
  # Write your code here
  n=len(arrayOne)
  m=len(arrayTwo)
  min=abs(arrayOne[0]-arrayTwo[0])
  for i in range(n):
      for j in range(0,m):
          if abs(arrayOne[i]-arrayTwo[j])<min:
              min=abs(arrayOne[i]-arrayTwo[j])
              l=[arrayOne[i],arrayTwo[j]]
  return l 


if __name__ == "__main__":
  arrayOne = [-1, 5, 10, 20, 28, 3]
  arrayTwo = [26, 134, 135, 15, 17]
  print(smallestDifference(arrayOne, arrayTwo))
