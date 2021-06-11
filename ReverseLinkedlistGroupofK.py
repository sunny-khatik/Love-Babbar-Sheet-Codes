#Code library 
class Solution:
    def reverse(self,head, k):
        # Code here
        if head is None:
            return None
        prev,nxt=None ,None
        curr= head
        tmp = k
        while curr != None and tmp:
            nxt=curr.next
            curr.next = prev
            prev =curr
            curr = nxt
            tmp-=1
        if nxt is not None:
            head.next=self.reverse(nxt,k)
        return prev
