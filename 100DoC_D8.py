def LongestPeak(a): 
  # Write your code here
  result=0
  n=len(a)
  start=0
  while start < n:
    end=start
    if end+1<n and a[end]<a[end+1]:
      while end+1<n and a[end]<a[end+1]:
        end+=1
      if end+1<n and a[end]>a[end+1]:
        while end+1<n and a[end]>a[end+1]:
          end+=1
        result=max(result,end-start+1)
    start=max(end,start+1)
  return result
  


if __name__ == "__main__":
  d = [1, 3, 1, 4, 5, 6,  
        7, 8, 9, 8, 7, 6, 5 ]
  print(LongestPeak(d)) 
      
