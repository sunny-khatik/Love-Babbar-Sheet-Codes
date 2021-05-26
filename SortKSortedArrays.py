# see k sroted array question of aditya varma 
# https://practice.geeksforgeeks.org/problems/nearly-sorted-algorithm/0#
from heapq import heapify, heappush, heappop
for i in range(int(input())):
    n , k = map(int , input().split())
    l = list(map(int , input().split()))
    l.sort()
    heap=l[:k+1]
    heapify(heap)
    i = 0
    for j in l[k+1:]:
        l[i]=heappop(heap)
        i+=1
        heappush(heap , j)
    while heap:
        l[i]=heappop(heap)
        i+=1
    for i in l:
        print(i , end=" ")
    print()
