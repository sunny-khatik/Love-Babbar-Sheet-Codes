# https://practice.geeksforgeeks.org/problems/intersection-of-two-sorted-linked-lists/1
def findIntersection(a , b):
    res = None
    prev = None
    while a and b :
        if a.data == b.data:
            new = Node(a.data)
            if res == None:
                res=new
            else:
                prev.next=new
            prev=new
            a=a.next
            b=b.next
        elif a.data > b.data:
            b=b.next
        else:
            a=a.next
    return res
