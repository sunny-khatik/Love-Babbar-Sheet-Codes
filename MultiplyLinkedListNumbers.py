
# https://practice.geeksforgeeks.org/problems/multiply-two-linked-lists/1
def multiplyTwoList(head1, head2):
    # Code here
    n1,n2 = 0,0
    while head1 or head2:
        if head1 :
            n1= (n1*10 + head1.data)
            head1 = head1.next
        if head2 :
            n2= (n2*10 + head2.data)
            head2 = head2.next
    return (n1*n2)%MOD
