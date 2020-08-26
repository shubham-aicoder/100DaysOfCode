def canVisitAllRooms(rooms):
    queue = []
    visited = [False for i in rooms]
    queue = add_rooms(rooms,0,queue,visited)
    visited[0] = True
    while len(queue)>0:
        queue = add_rooms(rooms,queue[0],queue,visited)
        visited[queue[0]] = True
        queue.pop(0)
    return all(visited)
def add_rooms(rooms,index,queue,visited):
    for i in rooms[index]:
        if not visited[i]:
            queue.append(i)
    return queue
  
if __name__ == "__main__":
  rooms = [[1],[2],[3],[]]
  print(canVisitAllRooms(rooms))
  





