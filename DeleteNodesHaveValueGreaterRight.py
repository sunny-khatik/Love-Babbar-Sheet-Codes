# https://practice.geeksforgeeks.org/problems/delete-nodes-having-greater-value-on-right/1
# In this will do reverse of linked list and do opposite if next element smaller then the max or current max then will remove it
# see code library video for intution only 
#my own solution.
class Solution:
    def rev(self, t):
        prev = None
        nxt = None
        curr = t
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    def compute(self,head):
        #Your code here
        # return self.solve()
        head = self.rev(head)
        mx = head.data
        prev = head
        tmp=head.next
        while tmp:
            if tmp.data >= mx:
                mx= tmp.data
                prev = tmp
                tmp=tmp.next
            else:
                prev.next = tmp.next
                tmp=tmp.next
        return self.rev(head)
