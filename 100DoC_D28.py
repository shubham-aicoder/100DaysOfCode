import collections

def count_island(input_matrix):
    #write your code here
    if not input_matrix:
        return 0

    rows,cols=len(input_matrix),len(input_matrix[0])
    visit=set()
    islands=0

    def bfs(r,c):
        q=collections.deque()
        visit.add((r,c))
        q.append((r,c))

        while q:
            row,col=q.popleft()
            directions=[[1,0],[-1,0],[0,1],[0,-1]]

            for dr,dc in directions:
                r,c=row+dr,col+dc
                if(r) in range(rows) and (c) in range(cols) and input_matrix[r][c]=="1" and ((r,c) not in visit):
                    q.append((r,c))
                    visit.add((r,c))

    for r in range(rows):
        for c in range(cols):
            if input_matrix[r][c]=="1" and (r,c) not in visit:
                bfs(r,c)
                islands+=1
    return islands
                
if __name__ == "__main__":
  input_matrix = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
  ]
  print(count_island(input_matrix))




