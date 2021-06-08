# https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/kth-smallest-number-again-2/
for i in range(int(input())):
    n, q = map(int , input().split())
    intervals = list()
    for i in range(n):
        intervals.append(list(map(int , input().split())))
    intervals.sort()
    ind=0
    for i in range(1,len(intervals)):
        if intervals[ind][1] >= intervals[i][0]:
            intervals[ind][1]=max(intervals[ind][1] ,intervals[i][1])
        else:
            ind+=1
            intervals[ind]=intervals[i]
    presum=[]
    r = 0
    for i in range(ind+1):
        r+= (intervals[i][1]-intervals[i][0]+1)
        presum.append(r)
    for i in range(q):
        k = int(input())
        if k > r:
            print(-1)
        else:
            index = -1
            start , end = 0,len(presum)-1
            while start <= end:
                mid = start + (end-start)//2
                if presum[mid] == k:
                    index=mid
                    break
                elif presum[mid] > k:
                    index=mid
                    end=mid-1
                else:
                    start=mid+1
            if index > 0:
                ans = k-presum[index-1]-1
            else:
                ans = k-1
            print(intervals[index][0]+ans)
