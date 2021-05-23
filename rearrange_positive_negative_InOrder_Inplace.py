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


# without an Order but works only when same positive and negative Number needs modification in it
l = [ 2, 3, -4, -1, 6, -9  ]
i, j = 0, len(l)-1

while True:
    if i >= j:
        break
    if l[i] > 0 and l[j] <= 0:
        l[i], l[j]=l[j],l[i]
        i+=1
        j-=1
    elif l[i] < 0:
        i+=1
    elif l[j] >= 0:
        j-=1
print(l)
i=0
j = len(l)-1
while i < j:
    if i%2 == 0:
        l[i],l[j]=l[j],l[i]
    i+=1
    j-=1
print(l)
