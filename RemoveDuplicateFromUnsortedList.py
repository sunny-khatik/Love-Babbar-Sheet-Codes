class Solution:
    #Function to remove duplicates from unsorted linked list.
    def removeDuplicates(self, head):
        # code here
        # return head after editing list
        tmp=head
        d = {}
        d[tmp.data]=1
        while tmp.next:
            if tmp.next.data in d:
                tmp.next=tmp.next.next
            else:
                d[tmp.next.data]=1
                tmp=tmp.next
        return head
