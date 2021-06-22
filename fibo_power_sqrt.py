# log(n) time complexity b negative as well as positive but note important thing here.
# for negative b also answer is true
# https://www.geeksforgeeks.org/write-a-c-program-to-calculate-powxn/
# print('%.6f' %(power(x, y)))  --> print using float point last decimall point print 6 didgit after it
def solve(a,b):
    if (b) == 0:
        return 1
    tmp = solve(a,int(b/2))  #very important if -1//2 = -0.5 round it ti -1 again and again so it will go in loop
    if b%2 == 0:
        return tmp*tmp
    else:
        if b > 0:
            return a*tmp*tmp
        else:
            return (tmp*tmp)/a 

x, y = 8, -1  #works for both the cases.
print((solve(x, y)))




# nth fibonachi number using O(logn) approch
# golden ration number 
# https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/
def square_root(x):
    start, end = 0, x 
    for i in range(1000):
        mid=(start+end)/2  
        res=mid**2       
        if res==x:       
            break        
        elif res>x:      
            end=mid
        else:                  
            start=mid
    return mid

def power(a, b):
    if b == 0:
        return 1
    ans = power(a, int(b/2))
    if b%2 == 0:
        return ans*ans
    else:
        if b > 0:
            return a*ans*ans
        else:
            return (ans*ans)/a

def nthfibo(n):
    phi = square_root(5)#root5
    # print("phi", phi , )
    n -=1
    tmp = round((power((1 + phi)/2 , n))/phi) # ((1+root5)/2)^n
    print(tmp)
    
for i in range(1,17):
    print(i , end=" ")
    nthfibo(i)
    print()
