def bs1(arr,start ,end,x):
    res = -1
    while start <= end:
        mid = start + (end-start)//2
        if arr[mid] == x:
            res = mid
            end= mid-1
        elif arr[mid] < x:
            start = mid+1
        else:
            res=mid
            end=mid-1
    return res

def bs2(arr,start ,end,x):
    res = -1
    while start <= end:
        mid = start + (end-start)//2
        if arr[mid] == x:
            res=mid
            start=mid+1
        elif arr[mid] < x:
            res = mid
            start = mid+1
        elif arr[mid] > x:
            end = mid-1
    return res
    
def getSequence(Str):
	if(len(Str) == 0):
		empty = []
		empty.append(0)
		return empty
	ch = Str[0]
	subStr = Str[1:]
	subSequences = getSequence(subStr)
	res = []
	for val in subSequences:
		res.append(val)
		res.append(ch + val)
	return res

    
if __name__ == "__main__":
	n, a,b = map(int , input().split())
	l = list()
	for i in range(n):
		l.append(int(input()))
	s1 = getSequence(l[ :n//2])
	s2 = getSequence(l[n//2:])
	c =0
	s2.sort()
	for i in range(len(s1)):
		low = bs1(s2,0,len(s2)-1,a-s1[i])
		high = bs2(s2,0,len(s2)-1,b-s1[i])
		if high != -1 and low != -1:
		    c+=(high-low+1)
	print(c)
