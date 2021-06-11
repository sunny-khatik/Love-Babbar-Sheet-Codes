
# https://practice.geeksforgeeks.org/problems/add-1-to-a-number-represented-as-linked-list/1
class Solution:
    def addOne(self,head):
        #Returns new head of linked List.
        if head is None:
            return head
        last = None
        curr= head
        while curr.next is not None:
            #if 9 is not there then last has some value 
            
            if curr.data != 9:
                last=curr
            curr=curr.next
        #if last elemnt not 9 simply increament and return
        if curr.data != 9:
            curr.data=curr.data+1
            return head
        #if we have 99999 like then last never assigned so we add nodet front with 0
        if last == None:
            last = Node(0)
            last.next=head #assign list head to next of new node
            head=last #assign head to new list
        #if last has some value then simply incremnet and make last one zero.
        #3499 -> 3500
        last.data = last.data+1 #increment thevalue pf frony node to one
        last=last.next #move to 99999 make it all zero
        while last is not None:
            last.data=0
            last=last.next
        return head 
