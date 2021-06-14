# https://practice.geeksforgeeks.org/problems/segregate-even-and-odd-nodes-in-a-linked-list5035/1
class Solution:
    def divide(self, N, head):
        # code here
        odd = list() 
        even = list()
        tmp = head
        while tmp:
            if tmp.data%2 == 0:
                even.append(tmp.data)
            else:
                odd.append(tmp.data)
            tmp=tmp.next
        if len(even) == 0:
            return head
        if len(odd) == 0:
            return head
        head.data = even[0]
        tmp2 = head
        for i in range(1,len(even)):
            tmp2.next.data = even[i]
            tmp2=tmp2.next
        for j in odd:
            tmp2.next.data = j
            tmp2 = tmp2.next
        return head
