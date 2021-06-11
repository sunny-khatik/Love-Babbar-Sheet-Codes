#easy but see code if not equal then increamnet else remove link
def removeDuplicates(head):
    tmp=head
    if tmp is None:
        return head
    while tmp.next is not None:
        if tmp.data == tmp.next.data:
            tmp.next= tmp.next.next
        else:
            tmp=tmp.next
    return head
