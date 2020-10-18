class Node :
    def __init__ (self, data=None , next = None):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self , data):
        node = Node(data)
        if self.head is None:
            self.head = node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node

    def print_l(self):  #printing the elements
        if self.head is None:
            print('Your link list is empty.')
        else:
            temp = self.head
            while temp:
                print(temp.data,"->", end="")
                temp = temp.next
        # print(temp.data)
        
    def push(self, data):   #insert_at_beginig
        
        node = Node(data)
        node.next = self.head
        self.head = node
        
        return
    
    def get_length(self):  #return length of linked list.
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count+=1
        return count
    
    def remove_at_index(self, index):
        if index < 0 or index >= l.get_length():
            print('index out of range')
            return
        if index == 0:
            self.head = self.head.next
        else:
            c=0
            itr = self.head
            while itr:
                if c == index - 1:
                    itr.next = itr.next.next
                    break
                itr = itr.next
                c+=1
    
    def insert_at_index(self , index, data):
        if index < 0 or index >= l.get_length():
            print('index out of range')
            return
        if index == 0:
            l.insert_at_beginig(data)
        else:
            c = 0
            node = Node(data)
            itr = self.head
            while itr:
                if c == index - 1:
                    temp = itr.next
                    itr.next = node
                    node.next = temp
                itr = itr.next
                c+=1

if __name__ == "__main__":
    l = LinkedList()
    l.append(1)
    l.append(3)
    l.append(4)
    l.append(5)
    l.push(0)
    l.insert_at_index(2, 2)
    # l.remove_at_index(1)
    # l.remove_at_index(0)
    print(l.get_length())
    l.print_l()
