#https://practice.geeksforgeeks.org/problems/circular-linked-list/1
def isCircular(head):
    # Code here
    slow = head
    fast = head
    bool = False
    while slow and fast.next and fast.next.next:
        slow=slow.next
        fast=fast.next.next
        if slow == fast:
            bool = True
            break
    if slow == head and bool:
        return 1
    else:
        return 0
