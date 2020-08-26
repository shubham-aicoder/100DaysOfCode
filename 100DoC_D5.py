def bool2str(m_bool):
  if m_bool:
    return 'true'
  else:
    return 'false'
    
def isValidSubsequence(array, sequence):
    is_valid = False
    
    # Write your code here.
    l=[]
    for i in range(len(sequence)):
        try:
            l.append(array.index(sequence[i]))
        except:
          l.append(0)
    if l==sorted(l):
        is_valid=True
    return bool2str(is_valid)
  
if __name__ == "__main__":
  array = [ 5, 1, 22, 5, 6, -1, 8]
  subsequence = [1, 6, -1, 10]
  print(isValidSubsequence(array, subsequence))
  
