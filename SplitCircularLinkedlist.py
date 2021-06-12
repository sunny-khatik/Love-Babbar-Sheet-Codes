#https://practice.geeksforgeeks.org/problems/split-a-circular-linked-list-into-two-halves/1
class Solution:
    def splitList(self, head, head1, head2):
        #code here
        slow , fast= head,head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            #stop fast where it will gonaa move to the head pointer it is our middel value
            if fast.next == head or fast.next.next == head:
                break
        
        #just find the middel position
        head1 = head
        head2 = slow.next
        slow.next = head1
        tmp = head2
        while tmp.next != head:
            tmp=tmp.next
        tmp.next = head2
        return head1,head2
