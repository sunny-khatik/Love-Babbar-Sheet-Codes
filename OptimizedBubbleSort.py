#tutorial point
#simple with comparison when sorted ouput
def bubblesort(l, n):
    cmpa = 0
    for i in range(n):
        for j in range(n-i-1):
            cmpa+=1
            if l[j] > l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
    return cmpa
l =  [1,2,3,4,5,6,7,8,9]
swap=bubblesort(l,len(l))
print(l)
print(swap)
# output 
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 36


# optimised when sorted output comparison
def bubblesort(l, n):
    cmpa = 0
    flag = 1
    for i in range(n):
        if flag != 1:
            break
        flag = 0
        for j in range(n-i-1):
            cmpa+=1
            if l[j] > l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
                flag =1 
    return cmpa
l =  [1,2,3,4,5,6,7,8,9]
swap=bubblesort(l,len(l))
print(l)
print(swap)
# output 
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 8




