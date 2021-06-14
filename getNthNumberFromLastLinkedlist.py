# https://practice.geeksforgeeks.org/problems/nth-node-from-end-of-linked-list/1
def rev(h):
    prev,nxt = None , None
    curr = h
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev
def getNthFromLast(head,n):
    head = rev(head)
    while head and n:
        if n == 1:
            return head.data
        n-=1
        head=head.next
    return -1
