# https://practice.geeksforgeeks.org/problems/reverse-a-doubly-linked-list/1
def reverseDLL(head):
    #return head after reversing
    if head == None or head.next == None:
        return head
    tmp=None
    curr = head
    while curr:
        tmp=curr.prev
        curr.prev = curr.next
        curr.next = tmp
        curr = curr.prev
    head = tmp.prev
    return head
