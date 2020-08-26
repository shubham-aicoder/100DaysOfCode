class Node:
    # Singly linked node
    def __init__(self, data=None):
        self.data = data
        self.next = None
class singly_linked_list:
    def __init__(self):
        # Createe an empty list
        self.tail = None
        self.head = None
        self.count = 0
    def append_item(self, data):
        #Append items on the list
        cur=Node(data)
        if self.head is None:
            self.head=cur
            return
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=cur

    def search_item(self, val):
        # Search the list
        if self.head is None:   #list has no elements
            return False
        else:
            temp=self.head
            while temp is not None:
                if temp.data==val:
                    return True
                else:
                    temp=temp.next
            if temp is None:
                return False

if __name__ == "__main__":
  items = singly_linked_list()
  items.append_item('PHP')
  items.append_item('Python')
  items.append_item('C#')
  items.append_item('C++')
  items.append_item('Java')
  print(items.search_item('SQL'))
