# https://practice.geeksforgeeks.org/problems/sort-a-linked-list/1
class Solution:
    def getmid(self,head):
        if head == None:
            return head
        slow = head
        fast = head
        while fast.next  and fast.next.next:
            slow=slow.next
            fast= fast.next.next
        return slow
    
    def merge(self, a, b):
        result = None
        if a  == None:
            return b
        if b == None:
            return a
        if a.data < b.data:
            result = a
            result.next = self.merge(a.next,b)
        else:
            result = b
            result.next = self.merge(a, b.next)
        return result
    #Function to sort the given linked list using Merge Sort.
    def mergeSort(self, head):
        if head == None or head.next == None:
            return head
        mid = self.getmid(head)
        nxttomid = mid.next
        mid.next = None
        l = self.mergeSort(head)
        r = self.mergeSort(nxttomid)
        sortedlist = self.merge(l,r)
        return sortedlist
