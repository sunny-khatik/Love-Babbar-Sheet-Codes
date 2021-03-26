# find the first and last occurance of given x in log(n) time coplexity.
# face book interview question.
def bst(l , x):
    index = -1
    s = 0
    e = len(l) - 1
    while s <= e:
        mid = int(s + (e-s)//2)
        
        if l[mid] >= x:
            index = mid 
            e = mid - 1
        else:
            s = mid + 1
    return index
    
l = [5,7,7,7,7,7]
x = 7
start  = bst(l , x)
end = bst(l , x+1) - 1
print(start , end)
if start<= end:
    print(start , end)
else:
    print(-1, -1)
