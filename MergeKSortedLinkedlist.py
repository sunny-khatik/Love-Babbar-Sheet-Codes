# https://practice.geeksforgeeks.org/problems/merge-k-sorted-linked-lists/1
# code library has diffrent approches
def merge(self, a,b):
        if a == None:
            return b
        if b == None:
            return a
        res = None
        if a.data <= b.data:
            res = a
            res.next = self.merge(a.next , b)
        else:
            res = b
            res.next = self.merge(a, b.next)
        return res
    #Function to merge K sorted linked list.
    def mergeKLists(self,arr,k):
        last = k-1
        i = 0
        while last != 0:
            i = 0
            j = last
            while i < j:
                arr[i]=self.merge(arr[i] , arr[j])
                i+=1
                j-=1
                if i>= j:
                    last=j
        return arr[0]
