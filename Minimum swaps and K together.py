# https://practice.geeksforgeeks.org/problems/minimum-swaps-required-to-bring-all-elements-less-than-or-equal-to-k-together4847/1#
# see dhruv goyels video for the approch
# https://www.geeksforgeeks.org/minimum-swaps-required-bring-elements-less-equal-k-together/
def minSwap (arr, n, k) : 
    #Complete the function
    swap=0
    wSize=0
    for i in arr:
        if i <= k:
            wSize+=1
    c=0
    for i in arr[0:wSize]:
        if i > k:
            c+=1
    swap=c
    for i in range(1,n-wSize+1):
        if arr[i-1] > k:
            c-=1
        if arr[i+wSize-1] > k:
            c+=1
        swap=min(c,swap)
    return swap
