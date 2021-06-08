#https://www.spoj.com/problems/AGGRCOW/
def solve(start , end ,cow,l):
    res=-1
    while start <= end:
        mid = start + (end-start)//2
        if check(cow,l,mid):
            res=mid
            start=mid+1
        else:
            end=mid-1
    return res
def check(cow,l,mid):
    c=1
    left=l[0]
    for i in range(1,len(l)):
        if l[i]-left >= mid:
            c+=1
            left=l[i]
    return c>=cow
            
if __name__ == "__main__":
    for i in range(int(input())):
        n, m = map(int , input().split())
        l = list()
        for i in range(n):
            l.append(int(input()))
        l.sort()
        print(solve(l[0],l[n-1]-l[0],m,l))
        
    
