import collections
def return_diag(input_matrix):
    #write your code here
    diags = collections.defaultdict(list)
    res = list()
    for r in range(len(input_matrix)):
        for c in range(len(input_matrix[r])):
            diags[r+c].append(input_matrix[r][c])
        
    for key,diag in diags.items():
        if key%2 == 0:
            diag.reverse()
        res.extend(diag)
        
    return res

if __name__ == "__main__":
  input_matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
  ]
  print(return_diag(input_matrix))




