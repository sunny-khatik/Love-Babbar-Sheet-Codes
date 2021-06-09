# see dhruv goyels's rearrange the array in alternate positive negative number in order in costant space
l = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8 ]

def rotateRight(l, start, stop):
    start_ele = l[stop]
    for i in range(stop, start, -1):
        l[i]=l[i-1]
    l[start]=start_ele
n = len(l)
wrongI = -1
for i in range(n):
    if wrongI != -1:
        if (l[wrongI] >= 0 and l[i] < 0)  or (l[wrongI] < 0 and l[i]>= 0):
            rotateRight(l,wrongI,i)
            if i - wrongI >= 2:
                wrongI+=2
            else:
                wrongI=-1
    else:
        if (l[i] < 0 and i%2 == 1 ) or( l[i]>= 0 and i%2 == 0):
            wrongI = i
            
print(l)
#solution corner negative elemnt and postive element
def rearrange(l,n):
    low=0
    high=n-1
    while low <= high:
        if l[low] > 0 and l[high] < 0:
            l[low],l[high]=l[high],l[low]
            low+=1
            high-=1
        elif l[low] > 0 and l[high] > 0:
            high-=1
        elif l[high] < 0 and l[low] < 0:
            low+=1
        else:
            low+=1
            high-=1
    print(l)
arr = [-1, -2, 3, 4, -5, 6, -7, -8, -9]
n = len(arr)
rearrange(arr, n)
#solution 3
def rearrange(l,n):
    low=0
    high=n-1
    while low <= high:
        if l[low] > 0 and l[high] < 0:
            l[low],l[high]=l[high],l[low]
            low+=1
            high-=1
        elif l[low] > 0 and l[high] > 0:
            high-=1
        elif l[high] < 0 and l[low] < 0:
            low+=1
        else:
            low+=1
            high-=1
    print(l)
arr = [-1, -2, 3, 4, -5, 6, -7, -8, -9]
n = len(arr)
rearrange(arr, n)
