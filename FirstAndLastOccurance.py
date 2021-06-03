#aditya varma 
# https://practice.geeksforgeeks.org/problems/first-and-last-occurrences-of-x3116/1
def find(arr,n,x):
    # code here
    mn,mx = -1 , -1
    start = 0
    end = n-1
    while start <= end:
        mid = start + (end-start)//2
        if arr[mid] == x:
            mn = mid
            end = mid -1
        elif arr[mid] > x:
            end = mid -1
        else:
            start = mid +1
    start = 0
    end = n-1
    while start <= end:
        mid = start + (end-start)//2
        if arr[mid] == x:
            mx = mid
            start = mid + 1
        elif arr[mid] > x:
            end = mid -1
        else:
            start = mid +1
    return [mn , mx]
