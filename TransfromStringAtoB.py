# https://www.geeksforgeeks.org/transform-one-string-to-another-using-minimum-number-of-given-operation/
def solve(a,b):
    if set(a) != set(b):
        return -1
    res = 0
    n = len(a)
    i ,j= n-1, n-1
    while i >= 0:
        if a[i] == b[j]:
            i-=1
            j-=1
        elif ( i >= 0 and j >= 0) and (a[i] != b[j]):
            res+=1
            # print(i,j,a[i], b[j],res)
            i-=1
        
    return res
print(solve("kamlaben" , "bekamlan"))
