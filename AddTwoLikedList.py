# https://practice.geeksforgeeks.org/problems/add-two-numbers-represented-by-linked-lists/1
# 3 2 1
# 1 1
# ans = 332
class Solution:
    def rev(self, head):
        nxt=None
        prev=None
        curr=head
        while curr is not None:
            nxt = curr.next
            curr.next=prev
            prev = curr
            curr = nxt
        head =prev
        return head
        
    #Function to add two numbers represented by linked list.
    def addTwoLists(self, first, second):
        first = self.rev(first)
        second = self.rev(second)
        carry = 0
        prev = None
        tmpf = first
        tmps = second
        res = None
        prev = None
        while tmpf or tmps:
            s1 = 0 if tmpf is None else tmpf.data
            s2 = 0 if tmps is None else tmps.data
            sum = s1 + s2 + carry
            carry =1 if sum >= 10 else 0
            sum = sum if sum < 10 else sum%10
            new = Node(sum)
            if res == None:
                res = new
            else:
                prev.next = new 
            prev = new
            if tmpf != None:
                tmpf = tmpf.next 
            if tmps != None:
                tmps = tmps.next 
        if carry:
            new = Node(carry)
            prev.next=new
        res = self.rev(res)
        return res
