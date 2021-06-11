# https://practice.geeksforgeeks.org/problems/intersection-point-in-y-shapped-linked-lists/1
def intersetPoint(head1,head2):
    #code here
    c1,c2=0,0
    t1,t2=head1,head2
    while t1:
        c1+=1
        t1=t1.next
    while t2:
        c2+=1
        t2=t2.next
    diff = abs(c1-c2)
    if c1 >= c2:
        while diff:
            head1=head1.next
            diff-=1
        while head1 != head2:
            head1=head1.next
            head2=head2.next
        return head2.data
    else:
        while diff:
            head2=head2.next
            diff-=1
        while head1 != head2:
            head1=head1.next
            head2=head2.next
        return head1.data
