#code library solution
class Solution:
    #Function to remove a loop in the linked list.
    def removeLoop(self, head):
        s,f=head, head
        bool = True
        while s and f and f.next:
            s=s.next
            f=f.next.next
            if s == f:
                bool=False
                break
        if bool:
            return 
        if s == head:
            while f.next != s:
                f=f.next
            f.next=None
            return
        else:
            s = head
            while s.next != f.next:
                s=s.next
                f=f.next
            f.next=None
            return
            
     
#new Code Metho hashing method.
def removeLoop(head):
    prev = None
    temp = head
    s = set()
    while temp:
        
        if temp in s:
            prev.next = None
            break
        else:
            s.add(temp)
            prev = temp
            temp = temp.next
