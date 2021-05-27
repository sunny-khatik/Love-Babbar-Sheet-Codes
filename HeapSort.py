#heap sort using max heap.
#in this if sort if we gonna change the sign of equation 1 and 2 then it will use mean heap and retrun array in desending order.
class Solution:
    def heapify(self,arr, n, i):
        largest = i
        l = 2*i + 1
        r = 2*i + 2
        if l < n and arr[l] > arr[largest]: #EQ=1  it check the left node if greater then update
            largest = l
        if r < n and arr[r] > arr[largest]: #EQ=2 it check the right node if greater then update
            largest = r
        if largest != i:
            arr[i],arr[largest] = arr[largest],arr[i]
            self.heapify(arr,n,largest)
        

    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        for i in range((n//2)-1,-1,-1):
            self.heapify(arr,n,i)
        for i in range(n-1,0,-1):
            arr[i],arr[0]=arr[0],arr[i]
            self.heapify(arr,i,0) # remember this point
