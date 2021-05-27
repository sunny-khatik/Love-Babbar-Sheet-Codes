#User function Template for pytho

def maxProfit( merged, a, b, n, m):
    for i in range(n):
        merged[i]=a[i]
    for i in range(m):
        merged[n+i]=b[i]
    heap(merged,m+n)
    
def heap(arr , n):
    for i in range((n//2)-1, -1 , -1):
        heapify(arr,n,i)
        
def heapify(arr,n,i):
    if i >= n:
        return 
    l = 2*i + 1
    r = 2*i + 2
    largest = i
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[largest],arr[i]=arr[i],arr[largest]
        heapify(arr,n,largest)
        
def main():
    T = int(input())
    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m = sz[0], sz[1]
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        merged = [0]*(n+m)
        
        maxProfit(merged, a, b, n, m)
        print(*merged)
        T -= 1
        
if __name__ == "__main__":
    main()

