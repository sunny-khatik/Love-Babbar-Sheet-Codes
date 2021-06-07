# https://www.geeksforgeeks.org/in-place-merge-sort/
def mergesort(start , end, arr):
    if start < end:
        mid = start + (end-start)//2
        mergesort(start, mid , arr)
        mergesort(mid+1 , end, arr)
        merge(start , end, arr)
def nextgap(n):
    if n == 0 or n == 1:
        return 0
    else:
        return n//2 + n%2
        
def merge(start , end , arr):
    gap = end-start+1
    gap = nextgap(gap)
    while gap > 0:
        i=start
        while i + gap <= end:
            j=i+gap
            if arr[i] > arr[j]:
                arr[i] , arr[j] = arr[j],arr[i]
            i+=1
        gap=nextgap(gap)

arr= [8,2,-6,4,0,1,-3,7]
mergesort(0 , len(arr)-1,arr)
print(arr)
