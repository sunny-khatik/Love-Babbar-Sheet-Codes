#code library nice solution
def solve(a,n,p,mid):
    time=0
    tmp_p=0
    for i in range(n):
        time = a[i+1]
        j=2
        while time <= mid:
            tmp_p+=1
            time+=(j*a[i+1])
            j+=1
        if tmp_p >= p:
            return 1
    return 0
if __name__ == "__main__":
    for i in range(int(input())):
        p = int(input())
        l = list(map(int , input().split()))
        start = 0
        end= 4e6+2
        ans=0
        while start <= end:
            mid = start + (end-start)//2
            if solve(l,l[0],p,mid):
                ans=mid
                end= mid-1
            else:
                start=mid+1
        print((ans))
