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
#another power version with mod recursive
class Solution:
    # (x^n)%d
    def pow(self, x, n, d):
        x = x%d
        if x == 0:
            return 0
        return self.solve(x,n,d)
    
    def solve(self, a,b,MOD):
        if b == 0:
            return 1
        tmp = self.solve(a,b//2,MOD)
        tmp=  tmp%MOD
        if b&1:
            return (tmp*tmp*a)%MOD
        else:
            return (tmp*tmp)%MOD
        
#power with mod iterative
class Solution:
    # (x^n)%d
    def pow(self, x,y,p):
        x = x%p
        if x == 0:
            return 0
        res = 1
        while y >0:
            if y&1 == 1:
                res = (res*x)%p
            y = y >> 1
            x = (x*x)%p
        return (res)
        
        
#sqrt of int return floor value
import math
class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        start = 0
        end = A
        ans= 0
        for i in range(100):
            mid = (start)+ ((end-start)/2)
            if mid*mid == A:
                ans=mid
                break
            elif mid*mid > A:
                end=mid-1
            else:
                ans = mid
                start = mid+1
        return math.floor(ans)


# nth fibonachi number using O(logn) approch
# golden ration number 
# https://www.geeksforgeeks.org/program-for-nth-fibonacci-number/
def square_root(x):
    start, end = 0, x 
    for i in range(100):
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
