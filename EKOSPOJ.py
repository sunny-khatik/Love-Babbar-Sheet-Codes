# https://www.spoj.com/problems/EKO/
def solve(start , end ,l, req):
    res=-1
    while start <= end:
        mid = start + (end-start)//2
        if check(m,l,mid):
            res=mid
            start=mid+1
        else:
            end=mid-1
    return res
def check(m,l,mid):
    s=0
    for i in l:
        if i >= mid:
            s+=(i-mid)
    return s >= m
    
if __name__ == "__main__":
    n, m = map(int , input().split())
    l = list(map(int , input().split()))
    print(solve(0, max(l), l , m))
    
