# https://practice.geeksforgeeks.org/problems/clone-a-linked-list-with-next-and-random-pointer/1
class Solution:
    def copyList(self, head):
        tmp=head
        while tmp != None:
            new = Node(tmp.data)
            nxtnxt = tmp.next
            tmp.next = new
            new.next = nxtnxt
            tmp=tmp.next.next
        tmp= head
        while tmp != None:
            if tmp.arb != None:
                tmp.next.arb = tmp.arb.next
            tmp=tmp.next.next
        tmp = head
        org = head
        copy = head.next
        ret = head.next
        while org.next and copy.next:
            org.next = org.next.next
            copy.next = copy.next.next
            org=org.next
            copy = copy.next
        org.next = None
        copy.next = None
        return ret
