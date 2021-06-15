# simple Quick sort
# jenny video
def Quicksort(l, lb , up):
    if lb < up:
        pivot = findPiv(l, lb,up)
        Quicksort(l, lb,pivot-1)
        Quicksort(l, pivot+1,up)
        
def findPiv(l,start,end):
    pivot = l[start]
    tmp = start
    while start < end:
        while start < len(l) and l[start] <= pivot:
            start+=1
        while l[end] > pivot:
            end-=1
        if start < end:
            l[start],l[end]=l[end],l[start]
    l[end] , l[tmp]=l[tmp],l[end]
    return end


l = [7,10,2,1,9,10,15,12]
Quicksort(l, 0,len(l)-1)
print(l)

#just go for random pivot it is optimized then
import random
def Quicksort(l, lb , up):
    if lb < up:
        pivot = findPiv(l, lb,up)
        Quicksort(l, lb,pivot-1)
        Quicksort(l, pivot+1,up)
        
def findPiv(l,start,end):
    pivot = l[random.randint(start,end)]
    tmp = start
    while start < end:
        while start < len(l) and l[start] <= pivot:
            start+=1
        while l[end] > pivot:
            end-=1
        if start < end:
            l[start],l[end]=l[end],l[start]
    l[end] , l[tmp]=l[tmp],l[end]
    return end

l = [7,10,2,1,9,10,15,12]
Quicksort(l, 0,len(l)-1)
print(l)
