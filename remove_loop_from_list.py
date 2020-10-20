# https://www.youtube.com/watch?v=JsVGDy0u1u8
# video for understanding
def rm(s , f, head):
    s = head
    while s != f:
        s = s.next
        f = f.next
    
    while f.next != s:
        f = f.next
    f.next = None

def removeLoop(head):
    s = head
    f = head
    while s and f and f.next:
        s = s.next
        f = f.next.next
        
        if s == f:
            rm(s , f, head)
            break
