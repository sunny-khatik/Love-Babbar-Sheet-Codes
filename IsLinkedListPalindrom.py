# https://practice.geeksforgeeks.org/problems/check-if-linked-list-is-pallindrome/1
class Solution:
    def rev(self,h):
        prev,nxt=None, None
        curr = h
        while curr != None:
            nxt = curr.next
            curr.next = prev
            prev=curr
            curr = nxt
        head=prev
        return head
        
    def isPalindrome(self, head):
        slow , fast = head,head
        prev=slow #slow becase when odd elemnt slow at middel so we have to take care of 
        #slow's prev we work according on even and odd.
        while fast.next and fast.next.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        h1 , h2 = None , None
        if fast.next != None: #if elemnt even
            h2 = slow.next
            slow.next = None
            h1 = head
        else: #elemnt is odd
            h2 = slow.next
            prev.next = None
            h1 = head
        h2=self.rev(h2)
        while h1 and h2:
            if h1.data != h2.data:
                return False
            h1 = h1.next
            h2 = h2.next
        return True
